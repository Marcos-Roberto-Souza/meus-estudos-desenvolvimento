import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { supabase } from "../services/supabase";

export default function FinalizarContagemPage() {

    const navigate = useNavigate();

    const [resumo, setResumo] = useState({
        categoria: "",
        totalProdutos: 0,
        produtosContados: 0,
        quantidadeTotal: 0,
        lotes: 0,
        percentual: 0
    });

    const [detalhesLotes, setDetalhesLotes] =
        useState<any[]>([]);

    useEffect(() => {
        carregarResumo();
    }, []);

    async function carregarResumo() {

        try {

            const contagemId =
                localStorage.getItem("contagemId");

            const produtos = JSON.parse(
                localStorage.getItem("listaProdutos") || "[]"
            );

            if (!contagemId) return;

            const {
                data: itens,
                error: itensError
            } = await supabase
                .from("contagem_itens")
                .select("*")
                .eq(
                    "contagem_id",
                    contagemId
                );

            if (itensError) {
                throw itensError;
            }

            const idsContagemItens =
                itens?.map(
                    (item) => item.id
                ) || [];

            let lotes: any[] = [];

            if (
                idsContagemItens.length > 0
            ) {

                const {
                    data: lotesData,
                    error: lotesError
                } = await supabase
                    .from("lotes")
                    .select(`*,
                        contagem_itens(
                            produto_id,
                            produtos (
                                nome
                            )
                        )
                    `)
                    .in(
                        "contagem_item_id",
                        idsContagemItens
                    );

                if (lotesError) {
                    throw lotesError;
                }

                lotes = lotesData || [];
            }

            console.log(
                "Contagem ID:",
                contagemId
            );

            console.log(
                "Itens:",
                itens
            );

            console.log(
                "Lotes:",
                lotes
            );

            setDetalhesLotes(
                lotes
            );

            const quantidadeTotal =
                itens?.reduce(
                    (
                        total,
                        item
                    ) =>
                        total +
                        Number(
                            item.quantidade || 0
                        ),
                    0
                ) ?? 0;

            const totalProdutos =
                produtos.length;

            const produtosContados =
                itens
                    ? new Set(
                        itens.map(
                            (item: any) =>
                                item.produto_id
                        )
                    ).size
                    : 0;

            const percentual =
                totalProdutos > 0
                    ? Math.min(
                        100,
                        Math.round(
                            (
                                produtosContados /
                                totalProdutos
                            ) * 100
                        )
                    )
                    : 0;

            const categoria =
                localStorage.getItem(
                    "categoriaNome"
                ) || "";

            setResumo({
                categoria,
                totalProdutos,
                produtosContados,
                percentual,
                quantidadeTotal,
                lotes: lotes.length
            });

        } catch (error) {

            console.error(
                "Erro ao carregar resumo:",
                error
            );

        }

    }

    async function finalizarContagem() {

        if (
            resumo.percentual < 100
        ) {

            alert(
                "Ainda existem produtos não contados."
            );

            return;
        }

        try {

            const contagemId =
                localStorage.getItem(
                    "contagemId"
                );

            if (!contagemId) return;

            const { error } =
                await supabase
                    .from("contagens")
                    .update({
                        status:
                            "FINALIZADA",
                        data_fim:
                            new Date().toISOString()
                    })
                    .eq(
                        "id",
                        contagemId
                    );

            if (error) {
                throw error;
            }

            localStorage.removeItem(
                "listaProdutos"
            );

            localStorage.removeItem(
                "contagemId"
            );

            localStorage.removeItem(
                "categoriaNome"
            );

            alert(
                "Contagem finalizada com sucesso!"
            );

            navigate("/home");

        } catch (error) {

            console.error(error);

            alert(
                "Erro ao finalizar a contagem."
            );

        }

    }

    return (

        <div
            style={{
                background: "#11153D",
                minHeight: "100vh",
                color: "white",
                padding: "30px"
            }}
        >

            <h1>
                ✅ Resumo da Contagem
            </h1>

            <div
                style={{
                    background: "#D8DFE8",
                    color: "#11153D",
                    padding: "25px",
                    borderRadius: "20px",
                    marginTop: "20px"
                }}
            >

                <p>
                    <strong>Categoria:</strong>{" "}
                    {resumo.categoria}
                </p>

                <p>
                    <strong>Total de Produtos:</strong>{" "}
                    {resumo.totalProdutos}
                </p>

                <p>
                    <strong>Produtos Contados:</strong>{" "}
                    {resumo.produtosContados}
                </p>

                <p>
                    <strong>Quantidade Total:</strong>{" "}
                    {resumo.quantidadeTotal}
                </p>

                <p>
                    <strong>Lotes:</strong>{" "}
                    {resumo.lotes}
                </p>

                <p>
                    <strong>Progresso:</strong>{" "}
                    {resumo.produtosContados}
                    /
                    {resumo.totalProdutos}
                    (
                    {resumo.percentual}
                    %)
                </p>

                <div
                    style={{
                        marginTop: "15px"
                    }}
                >
                    <div
                        style={{
                            background: "#DDD",
                            height: "12px",
                            borderRadius: "10px"
                        }}
                    >
                        <div
                            style={{
                                width: `${resumo.percentual}%`,
                                height: "12px",
                                background: "#39FF14",
                                borderRadius: "10px"
                            }}
                        />
                    </div>
                </div>

                <hr
                    style={{
                        margin: "25px 0"
                    }}
                />

                <h3>
                    Lotes Registrados
                </h3>

                {detalhesLotes.length === 0 && (
                    <p>
                        Nenhum lote registrado.
                    </p>
                )}

                {detalhesLotes.map(
                    (lote) => (

                        <div
                            key={lote.id}
                            style={{
                                background: "#FFF",
                                padding: "12px",
                                marginTop: "10px",
                                borderRadius: "10px"
                            }}
                        >
                            <p>
                                <strong>Produto:</strong>{" "}
                                {lote.contagem_itens?.produtos?.nome ?? "Produto não encontrado"}
                            </p>

                            <p>
                                <strong>Lote:</strong>{" "}
                                {lote.numero_lote}
                            </p>

                            <p>
                                <strong>Quantidade:</strong>{" "}
                                {lote.quantidade}
                            </p>

                            <p>
                                <strong>Validade:</strong>{" "}
                                {new Date(
                                    lote.validade
                                ).toLocaleDateString(
                                    "pt-BR"
                                )}
                            </p>

                            {lote.observacao && (

                                <p>
                                    <strong>
                                        Observação:
                                    </strong>{" "}
                                    {lote.observacao}
                                </p>

                            )}

                        </div>

                    )
                )}

            </div>

            <button
                onClick={
                    finalizarContagem
                }
                style={{
                    width: "100%",
                    marginTop: "30px",
                    padding: "15px",
                    fontSize: "18px",
                    fontWeight: "bold",
                    background: "#39FF14",
                    color: "#000",
                    border: "none",
                    borderRadius: "10px",
                    cursor: "pointer"
                }}
            >
                FINALIZAR CONTAGEM
            </button>

        </div>

    );

}