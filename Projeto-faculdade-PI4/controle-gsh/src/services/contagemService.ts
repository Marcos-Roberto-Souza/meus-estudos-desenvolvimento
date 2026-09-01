import { supabase } from "./supabase";

export async function salvarContagemItem(
    contagemId: string,
    produtoId: string,
    quantidade: number
) {

    const { data, error } = await supabase
        .from("contagem_itens")
        .insert({
            contagem_id: contagemId,
            produto_id: produtoId,
            quantidade
        })
        .select()
        .single();

    if (error) throw error;

    return data;
}