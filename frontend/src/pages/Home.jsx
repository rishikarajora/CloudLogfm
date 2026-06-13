import MainLayout from "../layouts/MainLayout";
import { Box, Typography, Button } from "@mui/material";
import { Link } from "react-router-dom";
import heroBanner from "../assets/hero-banner.jpeg";

export default function Home() {
  return (
    <MainLayout>
      <Box
        sx={{
          height: 450,
          borderRadius: 5,
          overflow: "hidden",
          backgroundImage: `url(${heroBanner})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          position: "relative",
        }}
      >
        <Box
          sx={{
            position: "absolute",
            inset: 0,
            background:
              "linear-gradient(rgba(2,6,23,.5),rgba(2,6,23,.9))",
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            px: 6,
          }}
        >
          <Typography variant="h2" fontWeight="bold">
            CloudLogFM
          </Typography>

          <Typography
            variant="h5"
            sx={{ color: "#cbd5e1", mt: 2 }}
          >
            AI-Powered Incident Intelligence Platform
          </Typography>

          <Typography
            sx={{
              mt: 2,
              maxWidth: 700,
              color: "#94a3b8",
            }}
          >
            LogBERT • FAISS • Root Cause Analysis •
            Anomaly Detection • Retrieval Intelligence
          </Typography>

          <Box sx={{ mt: 4, display: "flex", gap: 2 }}>
            <Button
              component={Link}
              to="/dashboard"
              variant="contained"
            >
              Launch Dashboard
            </Button>

            <Button
              component={Link}
              to="/analyze"
              variant="outlined"
            >
              Analyze Incident
            </Button>
          </Box>
        </Box>
      </Box>
    </MainLayout>
  );
}