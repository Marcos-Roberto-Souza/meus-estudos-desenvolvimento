import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { supabase } from "../services/supabase";

export default function HomePage() {

    const navigate = useNavigate();

    const [loading, setLoading] =
        useState(false);

    const [contagemIniciada, setContagemIniciada] =
        useState(
            !!localStorage.getItem("contagemId")
        );

    async function iniciarContagem() {

        try {

            setLoading(true);

            const { data: contagemExistente, error } =
                await supabase
                    .from("contagens")
                    .select("*")
                    .eq("status", "EM_ANDAMENTO")
                    .maybeSingle();

            if (error) {
                throw error;
            }

            if (contagemExistente) {

                localStorage.setItem(
                    "contagemId",
                    contagemExistente.id
                );

            } else {

                const { data: novaContagem, error: erroNova } =
                    await supabase
                        .from("contagens")
                        .insert({
                            status: "EM_ANDAMENTO",
                            data_inicio:
                                new Date().toISOString(),

                            // Substituir pelos UUIDs reais
                            concessao_id:
                                "339b9cd0-c1e4-4bdb-ad29-2974ad369a80",

                            usuario_id:
                                "7745a7d8-130b-4572-a3b9-3726f5c8244f"
                        })
                        .select()
                        .single();

                if (erroNova) {
                    throw erroNova;
                }

                localStorage.setItem(
                    "contagemId",
                    novaContagem.id
                );
            }

            setContagemIniciada(true);

            alert(
                "Contagem iniciada com sucesso!"
            );

        } catch (error) {

            console.error(error);

            alert(
                "Erro ao iniciar contagem."
            );

        } finally {

            setLoading(false);

        }

    }

    return (

        <div
            style={{
                background: "#11153D",
                minHeight: "100vh",
                color: "white",
                textAlign: "center",
                paddingTop: "80px"
            }}
        >

            <h1>
                CONTROLE DE ESTOQUE
            </h1>

            {!contagemIniciada && (

                <button
                    onClick={iniciarContagem}
                    disabled={loading}
                    style={{
                        marginTop: "30px",
                        padding: "15px 30px",
                        fontSize: "18px",
                        fontWeight: "bold",
                        borderRadius: "10px",
                        border: "none",
                        background: "#39FF14",
                        color: "#000",
                        cursor: "pointer"
                    }}
                >
                    {loading
                        ? "INICIANDO..."
                        : "INICIAR CONTAGEM"}
                </button>

            )}

            {contagemIniciada && (

                <div
                    style={{
                        marginTop: "50px",
                        display: "flex",
                        flexDirection: "column",
                        gap: "20px",
                        alignItems: "center"
                    }}
                >

                    <h2>
                        Escolha uma Categoria
                    </h2>

                    <button
                        onClick={() =>
                            navigate("/produtos/1")
                        }
                        style={{
                            width: "250px",
                            padding: "15px",
                            fontSize: "18px",
                            fontWeight: "bold",
                            borderRadius: "10px",
                            border: "none"
                        }}
                    >
                        BEBIDAS
                    </button>

                    <button
                        onClick={() =>
                            navigate("/produtos/2")
                        }
                        style={{
                            width: "250px",
                            padding: "15px",
                            fontSize: "18px",
                            fontWeight: "bold",
                            borderRadius: "10px",
                            border: "none"
                        }}
                    >
                        ALIMENTOS
                    </button>

                    <button
                        onClick={() =>
                            navigate("/produtos/3")
                        }
                        style={{
                            width: "250px",
                            padding: "15px",
                            fontSize: "18px",
                            fontWeight: "bold",
                            borderRadius: "10px",
                            border: "none"
                        }}
                    >
                        SORVETES
                    </button>

                </div>

            )}

        </div>

    );

}