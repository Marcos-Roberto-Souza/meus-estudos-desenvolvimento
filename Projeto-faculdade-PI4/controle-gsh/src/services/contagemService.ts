import { supabase } from "./supabase";

export async function salvarContagemItem(
    contagemId: string,
    produtoId: string,
    quantidade: number
) {

    const { data: existente } =
        await supabase
            .from("contagem_itens")
            .select("*")
            .eq("contagem_id", contagemId)
            .eq("produto_id", produtoId)
            .maybeSingle();

    if (existente) {

        console.log(
            "Registro existente:",
            existente
        );

        const { data, error } =
            await supabase
                .from("contagem_itens")
                .update({
                    quantidade,
                    contado: true
                })
                .eq("id", existente.id)
                .select()
                .maybeSingle();

        if (error) throw error;

        return data;
    }

    const { data, error } =
        await supabase
            .from("contagem_itens")
            .insert({
                contagem_id: contagemId,
                produto_id: produtoId,
                quantidade,
                contado: true
            })
            .select()
            .maybeSingle();

    if (error) throw error;

    return data;
}
export async function listarProdutosContados(
    contagemId: string
) {

    const { data, error } = await supabase
        .from("contagem_itens")
        .select("produto_id")
        .eq("contagem_id", contagemId);

    if (error) throw error;

    return data;
}


