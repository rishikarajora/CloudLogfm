import {
  Card,
  CardContent,
  Typography,
} from "@mui/material";

export default function MetricCard({
  title,
  value,
}) {
  return (
    <Card
      sx={{
        borderRadius: 4,
        background:
          "linear-gradient(135deg,#1e293b,#334155)",
      }}
    >
      <CardContent>
        <Typography
          color="gray"
          variant="body2"
        >
          {title}
        </Typography>

        <Typography
          variant="h4"
          sx={{ mt: 1 }}
        >
          {value}
        </Typography>
      </CardContent>
    </Card>
  );
}