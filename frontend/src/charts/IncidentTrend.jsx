import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { day: "Mon", incidents: 12 },
  { day: "Tue", incidents: 18 },
  { day: "Wed", incidents: 9 },
  { day: "Thu", incidents: 24 },
  { day: "Fri", incidents: 17 },
  { day: "Sat", incidents: 32 },
  { day: "Sun", incidents: 20 },
];

export default function IncidentTrend() {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <XAxis dataKey="day" />
        <YAxis />
        <Tooltip />
        <Line
          type="monotone"
          dataKey="incidents"
          stroke="#3b82f6"
          strokeWidth={3}
        />
      </LineChart>
    </ResponsiveContainer>
  );
}