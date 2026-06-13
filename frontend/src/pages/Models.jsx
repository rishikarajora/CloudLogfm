import MainLayout from "../layouts/MainLayout";
import { Box, Typography } from "@mui/material";

export default function Models() {
  const cards = [
    "LogBERT Foundation Model",
    "Next Event Predictor",
    "FAISS Retrieval Engine",
    "Root Cause Engine",
  ];

  return (
    <MainLayout>
      <Typography variant="h3" mb={4}>
        AI Models
      </Typography>

      <Box
        sx={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(280px,1fr))",
          gap: 3,
        }}
      >
        {cards.map((item) => (
          <Box
            key={item}
            sx={{
              p: 4,
              borderRadius: 4,
              background:
                "rgba(255,255,255,0.05)",
            }}
          >
            <Typography variant="h6">
              {item}
            </Typography>
          </Box>
        ))}
      </Box>
    </MainLayout>
  );
}