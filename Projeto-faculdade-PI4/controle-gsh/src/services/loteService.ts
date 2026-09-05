import { supabase } from "./supabase";

export interface Lote {
    numeroLote: string;
    quantidade: number;
    validade: string;
}

export async function salvarLote(
    contagemItemId: string,
    numeroLote: string,
    quantidade: number,
    validade: string,
    observacao: string
) {

    const { data, error } = await supabase
        .from("lotes")
        .insert({
            contagem_item_id: contagemItemId,
            numero_lote: numeroLote,
            quantidade,
            validade,
            observacao

        })
        .select()
        .maybeSingle();

    if (error) throw error;

    return data;
}