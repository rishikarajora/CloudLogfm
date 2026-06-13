import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";
import MetricCard from "../components/MetricCard";

import IncidentTrend from "../charts/IncidentTrend";
import SeverityChart from "../charts/SeverityChart";

import {
  Box,
  Typography,
  Chip,
} from "@mui/material";

import heroBanner from "../assets/hero-banner.jpeg";

export default function Dashboard() {

  const [stats, setStats] = useState({
    critical: 0,
    averageScore: 0,
    repositorySize: 0,
    latestSeverity: "N/A",
  });

  const [recentIncidents, setRecentIncidents] =
    useState([]);

  useEffect(() => {

    const incidents =
      JSON.parse(
        localStorage.getItem(
          "incidents"
        )
      ) || [];

    const critical =
      incidents.filter(
        (i) =>
          i.severity === "CRITICAL"
      ).length;

    const repositorySize =
      incidents.length;

    const averageScore =
      incidents.length > 0
        ? (
            incidents.reduce(
              (sum, i) =>
                sum + i.score,
              0
            ) / incidents.length
          ).toFixed(3)
        : "0";

    const latestSeverity =
      incidents.length > 0
        ? incidents[0].severity
        : "N/A";

    setStats({
      critical,
      averageScore,
      repositorySize,
      latestSeverity,
    });

    setRecentIncidents(
      incidents.slice(0, 5)
    );

  }, []);

  return (
    <MainLayout>

      {/* HERO SECTION */}

      <Box
        sx={{
          height: 350,
          borderRadius: 5,
          overflow: "hidden",
          position: "relative",
          backgroundImage: `url(${heroBanner})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          mb: 4,
          boxShadow:
            "0 10px 40px rgba(0,0,0,.4)",
        }}
      >
        <Box
          sx={{
            position: "absolute",
            inset: 0,

            background:
              "linear-gradient(rgba(2,6,23,.35),rgba(2,6,23,.90))",

            display: "flex",
            flexDirection: "column",
            justifyContent: "center",

            paddingLeft: 6,
          }}
        >
          <Typography
            variant="h2"
            fontWeight="bold"
          >
            CloudLogFM
          </Typography>

          <Typography
            variant="h5"
            sx={{
              mt: 1,
              color: "#cbd5e1",
            }}
          >
            AI-Powered Incident Intelligence Platform
          </Typography>

          <Typography
            sx={{
              mt: 2,
              color: "#94a3b8",
              maxWidth: 700,
            }}
          >
            LogBERT Foundation Model • Retrieval Engine •
            Root Cause Analysis • Anomaly Detection
          </Typography>

          <Box
            sx={{
              mt: 3,
              display: "flex",
              gap: 2,
              flexWrap: "wrap",
            }}
          >
            <Chip label="LogBERT" />
            <Chip label="FAISS Retrieval" />
            <Chip label="Root Cause AI" />
            <Chip label="Cloud Native" />
          </Box>
        </Box>
      </Box>

      {/* KPI CARDS */}

      <Box
        sx={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(250px,1fr))",
          gap: 3,
        }}
      >
        <MetricCard
          title="Critical Incidents"
          value={stats.critical}
        />

        <MetricCard
          title="Average Score"
          value={stats.averageScore}
        />

        <MetricCard
          title="Repository Size"
          value={stats.repositorySize}
        />

        <MetricCard
          title="Latest Severity"
          value={stats.latestSeverity}
        />
      </Box>

      {/* REPOSITORY STATUS */}

      <Box
        sx={{
          mt: 4,
          p: 4,
          borderRadius: 4,
          background:
            "rgba(255,255,255,.05)",

          border:
            "1px solid rgba(255,255,255,.08)",

          backdropFilter:
            "blur(12px)",
        }}
      >
        <Typography
          variant="h5"
          gutterBottom
        >
          Live Repository Status
        </Typography>

        <Typography>
          Total Incidents:
          {" "}
          {stats.repositorySize}
        </Typography>

        <Typography>
          Critical Incidents:
          {" "}
          {stats.critical}
        </Typography>

        <Typography>
          Latest Severity:
          {" "}
          {stats.latestSeverity}
        </Typography>
      </Box>

      {/* ANALYTICS */}

      <Box
        sx={{
          mt: 4,
          display: "grid",

          gridTemplateColumns: {
            xs: "1fr",
            lg: "2fr 1fr",
          },

          gap: 3,
        }}
      >
        <Box
          sx={{
            p: 3,
            borderRadius: 4,

            background:
              "rgba(255,255,255,.05)",

            backdropFilter:
              "blur(12px)",

            border:
              "1px solid rgba(255,255,255,.08)",
          }}
        >
          <Typography
            variant="h6"
            gutterBottom
          >
            Incident Trend
          </Typography>

          <IncidentTrend />
        </Box>

        <Box
          sx={{
            p: 3,
            borderRadius: 4,

            background:
              "rgba(255,255,255,.05)",

            backdropFilter:
              "blur(12px)",

            border:
              "1px solid rgba(255,255,255,.08)",
          }}
        >
          <Typography
            variant="h6"
            gutterBottom
          >
            Severity Distribution
          </Typography>

          <SeverityChart />
        </Box>
      </Box>

      {/* RECENT INCIDENTS */}

      <Box
        sx={{
          mt: 4,
          p: 4,
          borderRadius: 4,

          background:
            "rgba(255,255,255,.05)",

          border:
            "1px solid rgba(255,255,255,.08)",

          backdropFilter:
            "blur(12px)",
        }}
      >
        <Typography
          variant="h5"
          gutterBottom
        >
          Recent Incidents
        </Typography>

        {recentIncidents.length === 0 ? (
          <Typography
            sx={{
              color: "#94a3b8",
            }}
          >
            No incidents available.
          </Typography>
        ) : (
          recentIncidents.map(
            (incident) => (
              <Typography
                key={incident.id}
                sx={{
                  mb: 1,

                  color:
                    incident.severity ===
                    "CRITICAL"
                      ? "#ef4444"
                      : "#f59e0b",
                }}
              >
                ● {incident.severity}
                {" - "}
                {incident.rootCause}
              </Typography>
            )
          )
        )}
      </Box>

      {/* PLATFORM OVERVIEW */}

      <Box
        sx={{
          mt: 4,
          p: 4,
          borderRadius: 4,

          background:
            "rgba(255,255,255,.05)",

          border:
            "1px solid rgba(255,255,255,.08)",

          backdropFilter:
            "blur(12px)",
        }}
      >
        <Typography
          variant="h5"
          gutterBottom
        >
          Platform Overview
        </Typography>

        <Typography
          sx={{
            color: "#94a3b8",
            lineHeight: 1.8,
          }}
        >
          CloudLogFM continuously analyzes
          cloud infrastructure logs using
          LogBERT, anomaly detection,
          retrieval augmented incident
          intelligence and AI powered root
          cause analysis.
        </Typography>
      </Box>

      <Box
  sx={{
    mt: 4,
    p: 4,
    borderRadius: 4,

    background:
      "linear-gradient(135deg,#2563eb,#7c3aed)",

    boxShadow:
      "0 15px 40px rgba(59,130,246,.35)",
  }}
>
  <Typography
    variant="h5"
    fontWeight="bold"
  >
    AI Incident Assistant
  </Typography>

  <Typography sx={{ mt: 1 }}>
    Analyze anomalies, retrieve
    similar incidents and perform
    automated root cause analysis.
  </Typography>
</Box>

    </MainLayout>
  );
}
