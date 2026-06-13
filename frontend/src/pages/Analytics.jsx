import MainLayout from "../layouts/MainLayout";
import IncidentTrend from "../charts/IncidentTrend";
import SeverityChart from "../charts/SeverityChart";
import { Box, Typography } from "@mui/material";

export default function Analytics() {
  return (
    <MainLayout>
      <Typography variant="h3" mb={4}>
        Analytics
      </Typography>

      <Box
        sx={{
          display: "grid",
          gridTemplateColumns:
            "2fr 1fr",
          gap: 3,
        }}
      >
        <IncidentTrend />
        <SeverityChart />
      </Box>
    </MainLayout>
  );
}