import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { analyzeIncident } from "../api/incidentApi";
import ResultCard from "../components/ResultCard";

export default function Analyze() {
  const [sequence, setSequence] = useState(
    "10,12,14,20"
  );

  const [trueEvent, setTrueEvent] =
    useState("22");

  const [result, setResult] = useState(null);

  const [loading, setLoading] =
    useState(false);

  const handleAnalyze = async () => {
    try {
      setLoading(true);

      const payload = {
        sequence: sequence
          .split(",")
          .map((x) => Number(x.trim()))
          .filter((x) => !isNaN(x)),

        true_event: Number(trueEvent),
      };

      const response =
  await analyzeIncident(payload);

setResult(response);

/* SAVE INCIDENT */

const existingIncidents =
  JSON.parse(
    localStorage.getItem("incidents")
  ) || [];

const newIncident = {
  id: `INC-${Date.now()}`,
  severity: response.severity,
  rootCause: response.root_cause,
  score: response.anomaly_score,
  confidence:
    response.root_confidence,
  timestamp:
    new Date().toLocaleString(),
};

existingIncidents.unshift(
  newIncident
);

localStorage.setItem(
  "incidents",
  JSON.stringify(
    existingIncidents
  )
);
    } catch (error) {
      console.error(error);
      alert("Analysis Failed");
    }

    setLoading(false);
  };

  return (
    <MainLayout>
      <h1>Incident Investigation</h1>

      <p>
        Analyze log event sequences using
        LogBERT + Incident Engine
      </p>

      <div
        style={{
          background: "#1e293b",
          padding: "25px",
          borderRadius: "16px",
          marginTop: "25px",
        }}
      >
        <h3>Event Sequence</h3>

        <textarea
          rows="6"
          value={sequence}
          onChange={(e) =>
            setSequence(e.target.value)
          }
          style={{
            width: "100%",
            padding: "12px",
            borderRadius: "10px",
            marginTop: "10px",
            background: "#0f172a",
            color: "white",
            border: "1px solid #334155",
          }}
        />

        <h3
          style={{
            marginTop: "20px",
          }}
        >
          True Event
        </h3>

        <input
          type="number"
          value={trueEvent}
          onChange={(e) =>
            setTrueEvent(e.target.value)
          }
          style={{
            width: "200px",
            padding: "10px",
            borderRadius: "8px",
            background: "#0f172a",
            color: "white",
            border: "1px solid #334155",
          }}
        />

        <br />

        <button
  onClick={handleAnalyze}
  style={{
    marginTop: "20px",

    padding: "14px 28px",

    borderRadius: "12px",

    border: "none",

    cursor: "pointer",

    fontWeight: "bold",

    background:
      "linear-gradient(135deg,#2563eb,#7c3aed)",

    color: "white",

    fontSize: "16px",

    boxShadow:
      "0 8px 25px rgba(59,130,246,.35)",
  }}
>
  Analyze Incident
</button>
      </div>

      {loading && (
        <h2
          style={{
            marginTop: "30px",
          }}
        >
          Running Analysis...
        </h2>
      )}

      {result && (
  <>
    {/* RESULT CARDS */}

    <div
      style={{
        marginTop: "30px",

        display: "grid",

        gridTemplateColumns:
          "repeat(auto-fit,minmax(250px,1fr))",

        gap: "20px",
      }}
    >
      <ResultCard
        title="Severity"
        value={result.severity}
      />

      <ResultCard
        title="Anomaly Score"
        value={result.anomaly_score.toFixed(4)}
      />

      <ResultCard
        title="Root Cause"
        value={result.root_cause}
      />

      <ResultCard
        title="Confidence"
        value={result.root_confidence}
      />
    </div>

    {/* SIMILAR INCIDENTS */}

    <div
      style={{
        marginTop: "25px",

        background:
          "rgba(255,255,255,.05)",

        border:
          "1px solid rgba(255,255,255,.08)",

        backdropFilter:
          "blur(12px)",

        borderRadius: "18px",

        padding: "24px",
      }}
    >
      <h2>
        Similar Incidents
      </h2>

      <div
        style={{
          display: "grid",
          gap: "12px",
        }}
      >
        {result.similar_incidents.map(
          (incident, index) => (
            <div
              key={index}
              style={{
                padding: "14px",

                borderRadius: "12px",

                background:
                  "#1e293b",
              }}
            >
              {incident}
            </div>
          )
        )}
      </div>
    </div>
  </>
)}
    </MainLayout>
  );
}