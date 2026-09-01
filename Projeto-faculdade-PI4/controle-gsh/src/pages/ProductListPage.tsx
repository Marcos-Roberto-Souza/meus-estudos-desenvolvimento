import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { listarProdutosPorCategoria } from "../services/produtoService";

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

    useEffect(() => {

        carregarProdutos();

    }, []);

    async function carregarProdutos() {

        try {

            console.log("Categoria Recebida:", categoriaId);

            const data =
                await listarProdutosPorCategoria(
                    Number(categoriaId)
                );

                console.log("Produtos Retornados:", data);

            setProdutos(data || []);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }
    }

    const produtosFiltrados = produtos.filter(
        (produto) =>
            produto.nome
                .toLowerCase()
                .includes(busca.toLowerCase())
    );

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
                        : "ALIMENTOS"}
                </h1>

                <p>
                    Escolha um item para registrar a contagem
                </p>
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
            </div>

            <div
                style={{
                    marginTop: "20px"
                }}
            >
                {loading && <p>Carregando...</p>}

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
                                background: "#D8DFE8",
                                color: "#11153D",
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