import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Analyze from "./pages/Analyze";
import Incidents from "./pages/Incidents";
import Models from "./pages/Models";
import Analytics from "./pages/Analytics";
import About from "./pages/About";

export default function App() {
  return (
    <Routes>

      <Route
        path="/"
        element={<Home />}
      />

      <Route
        path="/dashboard"
        element={<Dashboard />}
      />

      <Route
        path="/analyze"
        element={<Analyze />}
      />

      <Route
        path="/incidents"
        element={<Incidents />}
      />

      <Route
        path="/models"
        element={<Models />}
      />

      <Route
        path="/analytics"
        element={<Analytics />}
      />

      <Route
        path="/about"
        element={<About />}
      />

    </Routes>
  );
}