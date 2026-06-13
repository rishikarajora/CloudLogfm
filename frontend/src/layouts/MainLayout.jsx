import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";

export default function MainLayout({
  children,
}) {
  return (
    <div
      style={{
        display: "flex",
        minHeight: "100vh",

        background:
          "linear-gradient(135deg,#020617,#0f172a,#111827)",

        color: "white",
      }}
    >
      <Sidebar />

      <div
        style={{
          flex: 1,
        }}
      >
        <Topbar />

        <div
          style={{
            padding: "30px",
          }}
        >
          {children}
        </div>
      </div>
    </div>
  );
}