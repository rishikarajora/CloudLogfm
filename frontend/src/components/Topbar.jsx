import {
  Notifications,
  AccountCircle,
} from "@mui/icons-material";

export default function Topbar() {
  return (
    <div
      style={{
        height: "70px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",

        padding: "0 25px",

        background:
          "rgba(255,255,255,.04)",

        borderBottom:
          "1px solid rgba(255,255,255,.08)",

        backdropFilter:
          "blur(10px)",
      }}
    >
      <div>
        <h3
          style={{
            margin: 0,
            color: "white",
          }}
        >
          CloudLogFM Console
        </h3>

        <span
          style={{
            color: "#94a3b8",
            fontSize: "13px",
          }}
        >
          AI Incident Intelligence
        </span>
      </div>

      <div
        style={{
          display: "flex",
          gap: "20px",
          color: "white",
        }}
      >
        <Notifications />

        <AccountCircle />
      </div>
    </div>
  );
}