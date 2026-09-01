export interface Produto {
  id: string;
  nome: string;
  categoria_id: number;
  imagem_url?: string;
  controla_validade: boolean;
  ativo: boolean;
}