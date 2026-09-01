import { supabase } from "./supabase";

export async function listarProdutos() {

    const { data, error } = await supabase

        .from("produtos")

        .select("*")

        .eq("ativo", true)

        .order("nome");


    if (error) {
        throw error;
    }

    return data;

}


export async function listarProdutosPorCategoria(

    categoriaId: number

) {
    console.log("Filtro categoria:", categoriaId);

    const { data, error } = await supabase

        .from("produtos")

        .select("*")
    console.log("Data Bruta: ", data);
    console.log("Erro Bruto: ", error);

    //.eq("categoria_id", categoriaId)

    //.eq("ativo", true)

    //.order("nome");

    if (error) throw error;

    return data?.filter((produto) => produto.categoria_id === categoriaId);
}

export async function buscarProduto(
    texto: string
) {
    const { data, error } = await supabase
        .from("produtos")
        .select("*")
        .ilike("nome", `%${texto}%`);

    if (error) throw error;

    return data;
}

export async function buscarProdutoPorId(
    produtoId: string
) {
    const { data, error } = await supabase
        .from("produtos")
        .select("*")
        .eq("id", produtoId)
        .single();

    if (error) throw error;

    return data;
}