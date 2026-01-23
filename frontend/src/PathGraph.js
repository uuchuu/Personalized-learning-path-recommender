import React, { useEffect, useRef } from "react";
import * as echarts from "echarts";

export default function PathGraph() {
  const chartRef = useRef(null);

  useEffect(() => {
    fetch("/graphdata")
      .then(res => res.json())
      .then(data => {
        const chart = echarts.init(chartRef.current);

        const option = {
          title: {
            text: "学习路径关系图",
            left: "center"
          },
          tooltip: {},
          series: [
            {
              type: "graph",
              layout: "force",
              roam: true,
              label: {
                show: true,
                position: "right"
              },
              force: {
                repulsion: 200
              },
              data: data.nodes,
              edges: data.edges,
              emphasis: {
                focus: "adjacency",
                label: {
                  show: true
                }
              }
            }
          ]
        };

        chart.setOption(option);
      });
  }, []);

  return <div ref={chartRef} style={{ width: "100%", height: "600px" }} />;
}
