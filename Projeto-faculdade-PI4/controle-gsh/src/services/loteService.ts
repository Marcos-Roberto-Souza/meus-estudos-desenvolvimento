import { supabase } from "./supabase";

export async function salvarLote(
    contagemItemId: string,
    quantidade: number,
    validade: string
) {

    const { data, error } = await supabase
        .from("lotes")
        .insert({
            contagem_item_id: contagemItemId,
            quantidade,
            validade
        })
        .select()
        .single();

    if (error) throw error;

    return data;
}