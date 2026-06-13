import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

import App from "./App";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#3b82f6",
    },
    secondary: {
      main: "#8b5cf6",
    },
    background: {
      default: "#0f172a",
      paper: "#1e293b",
    },
  },
});

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <BrowserRouter>
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <App />
    </ThemeProvider>
  </BrowserRouter>
);