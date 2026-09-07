import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { listarProdutosPorCategoria } from "../services/produtoService";
import { listarProdutosContados } from "../services/contagemService";

interface Produto {
    id: string;
    nome: string;
    imagem_url?: string;
}

export default function ProductListPage() {

    const navigate = useNavigate();

    const { categoriaId } = useParams();
    const [produtos, setProdutos] = useState<Produto[]>([]);
    const [busca, setBusca] = useState("");
    const [loading, setLoading] = useState(true);
    const [contados, setContados] = useState<string[]>([]);

    useEffect(() => {

        carregarProdutos();
        carregarContados();

    }, [categoriaId]);

    async function carregarProdutos() {
        try {

            console.log("Categoria Recebida:", categoriaId);

            const data =
                await listarProdutosPorCategoria(
                    Number(categoriaId)
                );

            localStorage.setItem(
                "categoriaNome",
                categoriaId === "1" ? "BEBIDAS"
                    : categoriaId === "2" ? "ALIMENTOS"
                        : "SORVETES"
            );
            localStorage.setItem("listaProdutos", JSON.stringify(data));

            console.log("Produtos Retornados:", data);

            setProdutos(data || []);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }
    }

    async function carregarContados() {

        const CONTAGEM_ID = localStorage.getItem("contagemId");

        if (!CONTAGEM_ID) {
            console.error("Contagem ID não encontrado no localStorage.");

            return;
        }

        const itens =
            await listarProdutosContados(
                CONTAGEM_ID
            );

        setContados([
            ...new Set(
                itens.map(
                    (item: any) =>
                        item.produto_id
                )
            )
        ]
        );
    }


    const produtosFiltrados = produtos.filter(
        (produto) =>
            produto.nome
                .toLowerCase()
                .includes(busca.toLowerCase())

    );

    const produtosContados = new Set(contados).size;
    const percentual = produtos.length > 0 ? Math.min(100, (produtosContados / produtos.length) * 100) : 0;

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
                    background: "#D8DFE8",
                    borderRadius: "20px",
                    padding: "20px",
                    color: "#11153D"
                }}
            >
                <h2>CONTAGEM EM ANDAMENTO</h2>

                <h1>
                    {categoriaId === "1"
                        ? "BEBIDAS"
                        : categoriaId === "2"
                            ? "ALIMENTOS"
                            : "SORVETES"
                    }
                </h1>

                <p>
                    Escolha um item para registrar a contagem
                </p>
            </div>

            <div
                style={{
                    marginTop: "20px",
                    marginBottom: "20px"
                }}
            >
                <p>
                    {contados.length} / {produtos.length}
                    {" "}produtos contados
                </p>

                <div
                    style={{
                        height: "12px",
                        background: "#ddd",
                        borderRadius: "10px"
                    }}
                >
                    <div
                        style={{
                            width: `${percentual}%`,
                            height: "12px",
                            background: "#39FF14",
                            borderRadius: "10px",
                            transition: "0.3s"
                        }}
                    />
                </div>
            </div>

            <div
                style={{
                    marginTop: "20px",
                    display: "flex",
                    gap: "10px"
                }}
            >
                <input
                    type="text"
                    placeholder="Buscar item"
                    value={busca}
                    onChange={(e) =>
                        setBusca(e.target.value)
                    }
                    style={{
                        flex: 1,
                        padding: "12px",
                        borderRadius: "10px"
                    }}
                />

                <button
                    style={{
                        padding: "12px 20px"
                    }}
                >
                    Filtro
                </button>
                
                <button
                    onClick={() => navigate("/home")}
                    style={{
                        padding: "10px 15px",
                        borderRadius: "10px",
                        border: "none",
                        cursor: "pointer"
                    }}
                >
                    ← Voltar
                </button>
            </div>

            <div
                style={{
                    marginTop: "20px"
                }}
            >
                {loading && (
                    <p>Carregando...</p>
                )}

                {!loading &&
                    produtosFiltrados.map((produto) => (
                        <div
                            key={produto.id}
                            onClick={() =>
                                navigate(
                                    `/produto/${produto.id}`
                                )
                            }
                            style={{
                                background:
                                    contados.includes(produto.id)
                                        ? "#38EF7D"
                                        : "#D8DFE8",

                                color:
                                    contados.includes(produto.id)
                                        ? "#000"
                                        : "#11153D",

                                padding: "25px",
                                borderRadius: "20px",
                                marginBottom: "15px",
                                cursor: "pointer",
                                fontSize: "24px",
                                fontWeight: "bold"
                            }}
                        >
                            {produto.nome}
                        </div>
                    ))}
            </div>
        </div>
    );
}