import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "../pages/LoginPage";
import HomePage from "../pages/HomePage";
import ProductListPage from "../pages/ProductListPage";
import ProductCountPage from "../pages/ProductCountPage";
import FinalizarContagemPage from "../pages/FinalizarContagemPage";

export default function AppRoutes() {
    return (
        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<LoginPage />}
                />0
                <Route
                    path="/home"
                    element={<HomePage />}
                />
                <Route
                    path="/produtos/:categoriaId"
                    element={<ProductListPage />}
                />
                <Route
                    path="/produto/:produtoId"
                    element={<ProductCountPage />}
                />
                <Route
                    path="/finalizar-contagem"
                    element={<FinalizarContagemPage />}
                />

            </Routes>

        </BrowserRouter>
    );
}