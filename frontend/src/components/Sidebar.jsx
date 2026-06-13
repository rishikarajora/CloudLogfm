import { Link } from "react-router-dom";

import {
  Home,
  Dashboard,
  Search,
  Storage,
  Psychology,
  Insights,
  Info,
} from "@mui/icons-material";

import logo from "../assets/logo.png";

export default function Sidebar() {
  const menuStyle = {
    color: "white",
    textDecoration: "none",
    padding: "14px",
    borderRadius: "14px",
    display: "flex",
    alignItems: "center",
    gap: "12px",
    background: "rgba(255,255,255,0.05)",
    transition: ".3s",
  };

  return (
    <div
      style={{
        width: "280px",
        minHeight: "100vh",
        background: "rgba(2,6,23,.95)",
        backdropFilter: "blur(20px)",
        borderRight: "1px solid rgba(255,255,255,.08)",
        padding: "24px",
        position: "sticky",
        top: 0,
      }}
    >
      {/* LOGO */}

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "12px",
          marginBottom: "50px",
        }}
      >
        <img
          src={logo}
          alt="logo"
          width="55"
          height="55"
          style={{
            borderRadius: "12px",
          }}
        />

        <div>
          <h2
            style={{
              margin: 0,
              color: "white",
            }}
          >
            CloudLogFM
          </h2>

          <p
            style={{
              margin: 0,
              color: "#94a3b8",
              fontSize: "12px",
            }}
          >
            Incident Intelligence
          </p>
        </div>
      </div>

      {/* NAVIGATION */}

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "12px",
        }}
      >
        <Link to="/" style={menuStyle}>
          <Home />
          Home
        </Link>

        <Link to="/dashboard" style={menuStyle}>
          <Dashboard />
          Dashboard
        </Link>

        <Link to="/analyze" style={menuStyle}>
          <Search />
          Analyze
        </Link>

        <Link to="/incidents" style={menuStyle}>
          <Storage />
          Incidents
        </Link>

        <Link to="/models" style={menuStyle}>
          <Psychology />
          AI Models
        </Link>

        <Link to="/analytics" style={menuStyle}>
          <Insights />
          Analytics
        </Link>

        <Link to="/about" style={menuStyle}>
          <Info />
          About
        </Link>
      </div>

      {/* FOOTER */}

      <div
        style={{
          marginTop: "50px",
          padding: "16px",
          borderRadius: "14px",
          background: "rgba(59,130,246,.1)",
          border: "1px solid rgba(59,130,246,.2)",
        }}
      >
        <h4
          style={{
            margin: 0,
            marginBottom: "8px",
          }}
        >
          LogBERT Engine
        </h4>

        <p
          style={{
            margin: 0,
            color: "#94a3b8",
            fontSize: "13px",
          }}
        >
          Retrieval-Augmented Incident Intelligence
        </p>
      </div>
    </div>
  );
}