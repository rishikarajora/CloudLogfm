import { useEffect, useState } from "react";
import MainLayout from "../layouts/MainLayout";

import {
  Box,
  Typography,
  TextField,
  Button,
  Chip,
} from "@mui/material";

import DeleteIcon from "@mui/icons-material/Delete";

export default function Incidents() {

  const [incidents, setIncidents] =
    useState([]);

  const [search, setSearch] =
    useState("");

  const [filter, setFilter] =
    useState("ALL");

  useEffect(() => {

    const data =
      JSON.parse(
        localStorage.getItem(
          "incidents"
        )
      ) || [];

    setIncidents(data);

  }, []);

  const deleteIncident = (id) => {

    const updated =
      incidents.filter(
        (i) => i.id !== id
      );

    setIncidents(updated);

    localStorage.setItem(
      "incidents",
      JSON.stringify(updated)
    );
  };

  const clearRepository = () => {

    localStorage.removeItem(
      "incidents"
    );

    setIncidents([]);
  };

  const filteredIncidents =
    incidents.filter((incident) => {

      const matchesSearch =
        incident.id
          .toLowerCase()
          .includes(
            search.toLowerCase()
          );

      const matchesFilter =
        filter === "ALL"
          ? true
          : incident.severity ===
            filter;

      return (
        matchesSearch &&
        matchesFilter
      );
    });

  return (
    <MainLayout>

      <Typography
        variant="h3"
        gutterBottom
      >
        Incident Repository
      </Typography>

      <Typography
        sx={{
          color: "#94a3b8",
          mb: 4,
        }}
      >
        Historical incidents generated
        by CloudLogFM
      </Typography>

      {/* SEARCH */}

      <TextField
        fullWidth
        placeholder="Search Incident ID..."
        value={search}
        onChange={(e) =>
          setSearch(
            e.target.value
          )
        }
        sx={{
          mb: 3,
          input: {
            color: "white",
          },
        }}
      />

      {/* FILTERS */}

      <Box
        sx={{
          display: "flex",
          gap: 2,
          mb: 3,
          flexWrap: "wrap",
        }}
      >
        <Button
          variant={
            filter === "ALL"
              ? "contained"
              : "outlined"
          }
          onClick={() =>
            setFilter("ALL")
          }
        >
          All
        </Button>

        <Button
          color="error"
          variant={
            filter ===
            "CRITICAL"
              ? "contained"
              : "outlined"
          }
          onClick={() =>
            setFilter(
              "CRITICAL"
            )
          }
        >
          Critical
        </Button>

        <Button
          color="warning"
          variant={
            filter ===
            "WARNING"
              ? "contained"
              : "outlined"
          }
          onClick={() =>
            setFilter(
              "WARNING"
            )
          }
        >
          Warning
        </Button>
      </Box>

      {/* COUNT */}

      <Typography
        sx={{
          mb: 3,
          color: "#94a3b8",
        }}
      >
        Total Incidents:
        {" "}
        {
          filteredIncidents.length
        }
      </Typography>

      {/* INCIDENTS */}

      {filteredIncidents.length ===
      0 ? (
        <Box
          sx={{
            p: 5,
            borderRadius: 4,
            textAlign: "center",

            background:
              "rgba(255,255,255,.05)",
          }}
        >
          <Typography
            variant="h6"
          >
            No Incidents Found
          </Typography>
        </Box>
      ) : (
        filteredIncidents.map(
          (incident) => (
            <Box
              key={incident.id}
              sx={{
                p: 3,
                mb: 2,

                borderRadius: 4,

                background:
                  "rgba(255,255,255,.05)",

                border:
                  "1px solid rgba(255,255,255,.08)",

                backdropFilter:
                  "blur(12px)",
              }}
            >
              <Box
                sx={{
                  display: "flex",

                  justifyContent:
                    "space-between",

                  alignItems:
                    "center",
                }}
              >
                <Typography
                  variant="h6"
                >
                  {incident.id}
                </Typography>

                <Chip
                  label={
                    incident.severity
                  }
                  color={
                    incident.severity ===
                    "CRITICAL"
                      ? "error"
                      : "warning"
                  }
                />
              </Box>

              <Typography
                sx={{
                  mt: 2,
                }}
              >
                Root Cause:
                {" "}
                {
                  incident.rootCause
                }
              </Typography>

              <Typography>
                Score:
                {" "}
                {incident.score.toFixed(
                  4
                )}
              </Typography>

              <Typography>
                Confidence:
                {" "}
                {
                  incident.confidence
                }
              </Typography>

              <Typography
                sx={{
                  color:
                    "#94a3b8",
                }}
              >
                {
                  incident.timestamp
                }
              </Typography>

              <Button
                startIcon={
                  <DeleteIcon />
                }
                color="error"
                sx={{
                  mt: 2,
                }}
                onClick={() =>
                  deleteIncident(
                    incident.id
                  )
                }
              >
                Delete
              </Button>
            </Box>
          )
        )
      )}

      {/* CLEAR BUTTON */}

      {incidents.length >
        0 && (
        <Button
          color="error"
          variant="contained"
          onClick={
            clearRepository
          }
          sx={{
            mt: 3,
          }}
        >
          Clear Repository
        </Button>
      )}

    </MainLayout>
  );
}