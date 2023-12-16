import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import { createRoot } from "react-dom/client";

import App from "./components/App";
import Cart from "./components/Cart";
import Order from "./components/Order";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Home from "./components/Home";



const router = createBrowserRouter ([
    {
        path: "/",
        element: <Home />,
    },
    {
        path: "/Cart",
        element: <Cart />,
    },
    {
        path: "/Order",
        element: <Order />,
    },
    {
        path: "/Signup",
        element: <Signup />,
    },
    {
        path: "/Login",
        element: <Login />,
    },
])



const container = document.getElementById("root");
const root = createRoot(container);
root.render(<RouterProvider router={router} />);
