import React, { useEffect, useRef, useState } from "react";
import * as echarts from "echarts";

export default function PathGraph() {
  const chartRef = useRef(null);
  const [selectedNode, setSelectedNode] = useState(null);

  // ⚠️ 重要：当你把 App 装到手机上时，请把这里的 localhost 换成你电脑的局域网 IP
  // 例如：const API_BASE = "http://192.168.1.5:5000";
  const API_BASE = "http://localhost:5000"; 

  useEffect(() => {
    const fetchGraphData = async () => {
      try {
        const res = await fetch(`${API_BASE}/graphdata`);
        const data = await res.json();

        const chart = echarts.init(chartRef.current);
        const option = {
          title: {
            text: "🔍 智能学习路径推荐",
            left: "center",
            top: 20,
            textStyle: { color: '#333', fontSize: 18 }
          },
          tooltip: { trigger: 'item' },
          series: [
            {
              type: "graph",
              layout: "force",
              symbolSize: 60,
              roam: true, // 允许手机双指缩放和移动
              label: { show: true, position: "inside", fontSize: 12 },
              edgeSymbol: ["circle", "arrow"],
              edgeSymbolSize: [4, 10],
              force: {
                repulsion: 1000,
                edgeLength: 150
              },
              draggable: true,
              data: data.nodes,
              links: data.edges,
              lineStyle: { opacity: 0.9, width: 2, curveness: 0.1, color: '#aaa' },
              itemStyle: {
                color: '#5470c6',
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.3)'
              },
              emphasis: { focus: "adjacency", lineStyle: { width: 4 } }
            }
          ]
        };

        chart.setOption(option);

        // 核心交互：点击节点弹出详情（App 常用交互）
        chart.on('click', (params) => {
          if (params.dataType === 'node') {
            setSelectedNode(params.data);
          }
        });

        // 适配屏幕大小
        window.addEventListener("resize", () => chart.resize());
      } catch (error) {
        console.error("无法获取数据，请检查后端是否启动:", error);
      }
    };

    fetchGraphData();
  }, []);

  return (
    <div style={{ width: "100vw", height: "100vh", backgroundColor: "#f5f5f5", position: "relative" }}>
      {/* 图表容器 */}
      <div ref={chartRef} style={{ width: "100%", height: "80%" }} />

      {/* 底部详情卡片：增强 App 感 */}
      {selectedNode ? (
        <div style={styles.card}>
          <h3 style={{ margin: "0 0 10px 0", color: "#333" }}>📘 {selectedNode.name}</h3>
          <p style={{ fontSize: "14px", color: "#666" }}>
            这是根据你的目标 “AI” 推荐的必修课程。
          </p>
          <button style={styles.button} onClick={() => setSelectedNode(null)}>关闭详情</button>
        </div>
      ) : (
        <div style={styles.hint}>💡 点击节点查看课程详情</div>
      )}
    </div>
  );
}

// 简单的 App 风格样式
const styles = {
  card: {
    position: "absolute",
    bottom: "20px",
    left: "5%",
    right: "5%",
    backgroundColor: "#fff",
    padding: "20px",
    borderRadius: "15px",
    boxShadow: "0 -2px 10px rgba(0,0,0,0.1)",
    zIndex: 1000,
    animation: "slideUp 0.3s ease-out"
  },
  hint: {
    textAlign: "center",
    color: "#999",
    padding: "20px",
    fontSize: "14px"
  },
  button: {
    backgroundColor: "#5470c6",
    color: "#fff",
    border: "none",
    padding: "8px 15px",
    borderRadius: "5px",
    width: "100%"
  }
};
