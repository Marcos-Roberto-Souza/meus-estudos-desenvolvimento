import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { buscarProdutoPorId } from "../services/produtoService";
import { salvarContagemItem } from "../services/contagemService";
import { salvarLote } from "../services/loteService";

interface Produto {
    id: string;
    nome: string;
    imagem_url?: string | null;
    controla_validade?: boolean;
}

export default function ProductCountPage() {
    const { produtoId } = useParams();

    const navigate = useNavigate();

    const [produto, setProduto] = useState<Produto | null>(null);

    const [numeroLote, setNumeroLote] = useState("");
    const [quantidade, setQuantidade] = useState("");
    const [validade, setValidade] = useState("");
    const [observacao, setObservacao] = useState("");

    const [carregandoProduto, setCarregandoProduto] = useState(true);
    const [salvando, setSalvando] = useState(false);

    useEffect(() => {
        carregarProduto();
    }, [produtoId]);

    async function carregarProduto() {
        if (!produtoId) {
            alert("Produto não encontrado.");
            navigate("/home");
            return;
        }

        try {
            setCarregandoProduto(true);

            const data = await buscarProdutoPorId(produtoId);

            setProduto(data);

            // Limpa os campos quando muda para o próximo produto.
            setNumeroLote("");
            setQuantidade("");
            setValidade("");
            setObservacao("");

        } catch (error) {
            console.error("Erro ao carregar produto:", error);

            alert("Não foi possível carregar o produto.");
        } finally {
            setCarregandoProduto(false);
        }
    }

    async function salvar() {
        if (salvando) {
            return;
        }

        const numeroLoteLimpo = numeroLote.trim();
        const quantidadeNumerica = Number(quantidade);

        if (!produto) {
            alert("Produto não encontrado.");
            return;
        }

        if (!numeroLoteLimpo) {
            alert("Informe o número do lote.");
            return;
        }

        if (
            !quantidade ||
            !Number.isFinite(quantidadeNumerica) ||
            quantidadeNumerica <= 0
        ) {
            alert("Informe uma quantidade maior que zero.");
            return;
        }

        if (!validade) {
            alert("Informe a data de validade.");
            return;
        }

        const contagemId = localStorage.getItem("contagemId");

        if (!contagemId) {
            alert(
                "Nenhuma contagem em andamento. Volte ao início e clique em Iniciar Contagem."
            );

            navigate("/home");
            return;
        }

        try {
            setSalvando(true);

            console.log("1 - Iniciando salvamento");

            const contagemItem = await salvarContagemItem(
                contagemId,
                produto.id,
                quantidadeNumerica
            );

            if (!contagemItem?.id) {
                throw new Error(
                    "O item da contagem foi salvo, mas nenhum ID foi retornado."
                );
            }

            console.log(
                "2 - Item da contagem salvo:",
                contagemItem
            );

            const loteSalvo = await salvarLote(
                contagemItem.id,
                numeroLoteLimpo,
                quantidadeNumerica,
                validade,
                observacao
            );

            console.log("3 - Lote salvo:", loteSalvo);

            const produtos: Produto[] = JSON.parse(
                localStorage.getItem("listaProdutos") || "[]"
            );

            const indiceAtual = produtos.findIndex(
                (item) => item.id === produto.id
            );

            /*
             * Se o produto não estiver na lista, índiceAtual será -1.
             * Nesse caso, não devemos usar produtos[0] como próximo
             * produto sem perceber o erro.
             */
            if (indiceAtual === -1) {
                console.error(
                    "Produto atual não encontrado na listaProdutos.",
                    produto.id
                );

                navigate("/finalizar-contagem");
                return;
            }

            const proximoProduto = produtos[indiceAtual + 1];

            if (proximoProduto) {
                console.log(
                    "4 - Carregando próximo produto:",
                    proximoProduto.nome
                );

                navigate(`/produto/${proximoProduto.id}`);
                return;
            }

            console.log(
                "5 - Todos os produtos foram percorridos"
            );

            navigate("/finalizar-contagem");
        } catch (error: unknown) {
            console.error("Erro completo ao salvar:", error);

            if (error instanceof Error) {
                console.error("Mensagem:", error.message);
            }

            alert(
                "Não foi possível salvar o produto. Verifique os dados e tente novamente."
            );
        } finally {
            setSalvando(false);
        }
    }

    async function confirmarSaida() {

        const contagemId =
            localStorage.getItem("contagemId");

        if (!contagemId) {

            navigate(-1);
            return;

        }

        const confirmar = window.confirm(
            "Ao sair, a contagem atual será deletada. Deseja sair sem finalizar?"
        );

        if (confirmar) {

            localStorage.removeItem(
                "listaProdutos"

            );

            localStorage.removeItem("contagemId");
            localStorage.removeItem("listaProdutos");
            localStorage.removeItem("categoriaNome");

            navigate("/home");

        }

    }



    if (carregandoProduto) {
        return (
            <div
                style={{
                    background: "#11153D",
                    minHeight: "100vh",
                    color: "white",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    padding: "20px"
                }}
            >
                <p>Carregando produto...</p>
            </div>
        );
    }

    if (!produto) {
        return (
            <div
                style={{
                    background: "#11153D",
                    minHeight: "100vh",
                    color: "white",
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "center",
                    alignItems: "center",
                    padding: "20px"
                }}
            >
                <p>Produto não encontrado.</p>

                <button
                    type="button"
                    onClick={() => navigate("/home")}
                    style={{
                        marginTop: "20px",
                        padding: "12px 20px",
                        border: "none",
                        borderRadius: "10px",
                        cursor: "pointer"
                    }}
                >
                    VOLTAR AO INÍCIO
                </button>
            </div>
        );
    }

    return (
        <div
            style={{
                background: "#11153D",
                minHeight: "100vh",
                padding: "20px",
                color: "white"
            }}
        >
            <div
                style={{
                    width: "100%",
                    maxWidth: "600px",
                    margin: "0 auto"
                }}
            >
                <button
                    type="button"
                    onClick={confirmarSaida}
                    disabled={salvando}
                    style={{
                        padding: "10px 16px",
                        background: "transparent",
                        color: "white",
                        border: "1px solid white",
                        borderRadius: "10px",
                        cursor: salvando ? "not-allowed" : "pointer",
                        opacity: salvando ? 0.6 : 1
                    }}
                >
                    VOLTAR
                </button>

                <h1
                    style={{
                        marginTop: "30px"
                    }}
                >
                    {produto.nome}
                </h1>

                <p>
                    Informe os dados do lote encontrado para este produto.
                </p>

                <div
                    style={{
                        marginTop: "30px"
                    }}
                >
                    <label htmlFor="numero-lote">
                        Número do Lote
                    </label>

                    <input
                        id="numero-lote"
                        type="text"
                        value={numeroLote}
                        onChange={(event) =>
                            setNumeroLote(event.target.value)
                        }
                        placeholder="Exemplo: PEP240901A"
                        autoComplete="off"
                        disabled={salvando}
                        style={{
                            boxSizing: "border-box",
                            width: "100%",
                            padding: "15px",
                            marginTop: "10px",
                            border: "1px solid #CBD5E1",
                            borderRadius: "10px",
                            fontSize: "16px"
                        }}
                    />
                </div>

                <div
                    style={{
                        marginTop: "20px"
                    }}
                >
                    <label htmlFor="quantidade">
                        Quantidade
                    </label>

                    <input
                        id="quantidade"
                        type="number"
                        min="1"
                        step="1"
                        inputMode="numeric"
                        value={quantidade}
                        onChange={(event) =>
                            setQuantidade(event.target.value)
                        }
                        placeholder="Exemplo: 12"
                        disabled={salvando}
                        style={{
                            boxSizing: "border-box",
                            width: "100%",
                            padding: "15px",
                            marginTop: "10px",
                            border: "1px solid #CBD5E1",
                            borderRadius: "10px",
                            fontSize: "16px"
                        }}
                    />
                </div>

                <div
                    style={{
                        marginTop: "20px"
                    }}
                >
                    <label htmlFor="validade">
                        Data de Validade
                    </label>

                    <input
                        id="validade"
                        type="date"
                        value={validade}
                        onChange={(event) =>
                            setValidade(event.target.value)
                        }
                        disabled={salvando}
                        style={{
                            boxSizing: "border-box",
                            width: "100%",
                            padding: "15px",
                            marginTop: "10px",
                            border: "1px solid #CBD5E1",
                            borderRadius: "10px",
                            fontSize: "16px"
                        }}
                    />
                </div>
                <div
                    style={{
                        marginTop: "20px"
                    }}
                >
                    <label htmlFor="observacao">
                        Observação
                    </label>

                    <textarea
                        id="observacao"
                        value={observacao}
                        onChange={(event) =>
                            setObservacao(event.target.value)
                        }
                        placeholder="Ex: Caixa avariada, próximo do vencimento..."
                        disabled={salvando}
                        rows={4}
                        style={{
                            boxSizing: "border-box",
                            width: "100%",
                            padding: "15px",
                            marginTop: "10px",
                            border: "1px solid #CBD5E1",
                            borderRadius: "10px",
                            fontSize: "16px",
                            resize: "vertical"
                        }}
                    />
                </div>

                <button
                    type="button"
                    onClick={salvar}
                    disabled={salvando}
                    style={{
                        boxSizing: "border-box",
                        marginTop: "40px",
                        width: "100%",
                        padding: "15px",
                        background: salvando
                            ? "#94A3B8"
                            : "#39FF14",
                        color: "#000",
                        fontWeight: "bold",
                        fontSize: "18px",
                        border: "none",
                        borderRadius: "10px",
                        cursor: salvando
                            ? "not-allowed"
                            : "pointer"
                    }}
                >
                    {salvando
                        ? "SALVANDO..."
                        : "SALVAR E PRÓXIMO"}
                </button>
            </div>
        </div>
    );
}