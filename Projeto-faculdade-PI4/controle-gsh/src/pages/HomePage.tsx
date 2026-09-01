import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import { supabase } from "../services/supabase";

export default function HomePage() {

    const navigate = useNavigate();
    useEffect(() => {
        async function teste(){
            const { data, error } = await supabase
                .from("categorias")
                .select("*");

            console.log("DATA:", data);
            
            console.log("ERROR:", error);
        }
        teste();
    }, []);

    return (
        <div
            style={{
                background: "#11153D",
                minHeight: "100vh",
                color: "white",
                textAlign: "center",
                paddingTop: "100px"
            }}
        >
            <h1>INICIAL</h1>

            <button
                onClick={() => navigate("/produtos/2")}
            >
                ALIMENTOS
            </button>

            <button
                onClick={() => navigate("/produtos/1")}
            >
                BEBIDAS
            </button>
        </div>
    );
}