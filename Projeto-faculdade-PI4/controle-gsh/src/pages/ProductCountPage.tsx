import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { salvarContagemItem } from "../services/contagemService";
import { salvarLote } from "../services/loteService";
import { buscarProdutoPorId } from "../services/produtoService";

export default function ProductCountPage() {

    const { produtoId } = useParams();

    const [produto, setProduto] = useState<any>();

    const [quantidade, setQuantidade] =
        useState("");

    const [validade, setValidade] =
        useState("");

    useEffect(() => {

        carregarProduto();

    }, []);

    async function carregarProduto() {

        try {

            const data =
                await buscarProdutoPorId(
                    produtoId as string
                );

            setProduto(data);

        } catch (error) {

            console.error(error);

        }
    }

    async function salvar() {

        try {

            if (!quantidade) {

                alert("Informe a quantidade");

                return;
            }

            const CONTAGEM_ID =
                "899d6dac-71b8-4b22-9418-5b8b5d8d51c2";

            const contagemItem =
                await salvarContagemItem(
                    CONTAGEM_ID,
                    produto.id,
                    Number(quantidade)
                );

            if (validade) {

                await salvarLote(
                    contagemItem.id,
                    Number(quantidade),
                    validade
                );
            }

            alert("Registro salvo com sucesso!");

            setQuantidade("");
            setValidade("");

        } catch (error) {

            console.error(error);

            alert("Erro ao salvar");

        }
    }

    if (!produto) {

        return <p>Carregando...</p>;

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
            <h1>
                {produto.nome}
            </h1>

            <div
                style={{
                    marginTop: "30px"
                }}
            >
                <label>

                    Quantidade

                </label>

                <input
                    type="number"
                    value={quantidade}
                    onChange={(e) =>
                        setQuantidade(e.target.value)
                    }
                    style={{
                        width: "100%",
                        padding: "15px",
                        marginTop: "10px"
                    }}
                />
            </div>

            <div
                style={{
                    marginTop: "20px"
                }}
            >
                <label>

                    Data de Validade

                </label>

                <input
                    type="date"
                    value={validade}
                    onChange={(e) =>
                        setValidade(e.target.value)
                    }
                    style={{
                        width: "100%",
                        padding: "15px",
                        marginTop: "10px"
                    }}
                />
            </div>

            <button
                onClick={salvar}
                style={{
                    marginTop: "40px",
                    width: "100%",
                    padding: "15px",
                    background: "#39FF14",
                    color: "#000",
                    fontWeight: "bold",
                    fontSize: "18px"
                }}
            >
                SALVAR E PRÓXIMO
            </button>

        </div>
    );
}