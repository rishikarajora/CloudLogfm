export default function ResultCard({
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
      }}
    >
      <h4
        style={{
          color: "#94a3b8",
          marginBottom: "12px",
        }}
      >
        {title}
      </h4>

      <h2
        style={{
          margin: 0,
          color: "white",
        }}
      >
        {value}
      </h2>
    </div>
  );
}