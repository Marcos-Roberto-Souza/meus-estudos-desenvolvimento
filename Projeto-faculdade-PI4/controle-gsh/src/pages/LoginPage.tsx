import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {

  const navigate = useNavigate();

  const [encarregado, setEncarregado] = useState("");
  const [concessao, setConcessao] = useState("");

  function entrar() {

    if (!encarregado || !concessao) {

      alert("Preencha todos os campos");

      return;
    }

    localStorage.setItem(
      "encarregado",
      encarregado
    );

    localStorage.setItem(
      "concessao",
      concessao
    );

    navigate("/home");
  }

  return (
    <div
      style={{
        background: "#11153D",
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
      <div
        style={{
          width: 350,
          display: "flex",
          flexDirection: "column",
          gap: 20
        }}
      >
        <h1 style={{
          color: "white",
          textAlign: "center",
          fontSize: "35px"
        }}>CONTROLE DE VENDAS</h1>

        <input
          placeholder="ENCARREGADO"
          value={encarregado}
          onChange={(e) =>
            setEncarregado(e.target.value)
          }
        />

        <input
          placeholder="CONCESSÃO"
          value={concessao}
          onChange={(e) =>
            setConcessao(e.target.value)
          }
        />

        <button
          onClick={entrar}
          style={{
            background: "#39FF14",
            padding: "15px",
            fontWeight: "bold",
            fontSize: "20px",
            cursor: "pointer",
            border: "none",
            borderRadius: "10px"
          }}
        >
          ENTRAR
        </button>
      </div>
    </div>
  );
}