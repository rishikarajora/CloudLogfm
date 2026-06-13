import MainLayout from "../layouts/MainLayout";
import { Typography, Box } from "@mui/material";

export default function About() {
  return (
    <MainLayout>
      <Typography variant="h3">
        About CloudLogFM
      </Typography>

      <Box sx={{ mt: 4 }}>
        <Typography>
          CloudLogFM is a Retrieval-Augmented
          Incident Intelligence Platform for
          large-scale cloud systems.
        </Typography>

        <Typography sx={{ mt: 3 }}>
          Stack:
          React • FastAPI • PyTorch • FAISS •
          Drain3 • LogBERT
        </Typography>
      </Box>
    </MainLayout>
  );
}