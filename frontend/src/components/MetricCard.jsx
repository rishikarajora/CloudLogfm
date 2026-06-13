export default function MetricCard({
  title,
  value,
}) {
  return (
    <div
      style={{
        background:
          "rgba(255,255,255,0.05)",

        border:
          "1px solid rgba(255,255,255,0.08)",

        backdropFilter:
          "blur(12px)",

        padding: "24px",

        borderRadius: "18px",

        transition: "0.3s",

        boxShadow:
          "0 10px 30px rgba(0,0,0,.25)",
      }}
    >
      <h4
        style={{
          color: "#94a3b8",
          marginBottom: "12px",
          fontWeight: "500",
        }}
      >
        {title}
      </h4>

      <h1
        style={{
          margin: 0,
          color: "white",
          fontSize: "34px",
        }}
      >
        {value}
      </h1>
    </div>
  );
}