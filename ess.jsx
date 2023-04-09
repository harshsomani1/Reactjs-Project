import React from 'react';
import  data  from './data.json';
import { Group } from '@visx/group';
import { Bar } from '@visx/shape';
import { scaleLinear, scaleBand } from '@visx/scale';

// We'll use some mock data from `@visx/mock-data` for this.


// Define the graph dimensions and margins
const width = 700;
const height = 500;
const margin = { top: 10, bottom: 20, left: 20, right: 20 };

// Then we'll create some bounds
const xMax = width - margin.left - margin.right;
const yMax = height - margin.top - margin.bottom;

// We'll make some helpers to get at the data we want
const x = d => d.chemical;
const y = d => d.combined_score ;

// And then scale the graph by our data
const xScale = scaleBand({
  range: [0, xMax+1],
  round: true,
  domain: data.map(x),
  padding: 0.1,
});
const yScale = scaleLinear({
  range: [yMax,0],
  round: true,
  domain: [0, Math.max(...data.map(y))],
});

// Compose together the scale and accessor functions to get point functions
const compose = (scale, accessor) => data => scale(accessor(data));
const xPoint = compose(xScale, x);
const yPoint = compose(yScale, y);

// Finally we'll embed it all in an SVG
function BarGraph() {
  return (
    <svg width={width} height={height}>
      {data.map((d, i) => {
        const barHeight = (yMax - yPoint(d));
        return (
          <Group key={`bar-${i}`}>
            <Bar
              x={xPoint(d)}
              y={yMax - barHeight}
              height={barHeight}
              width={xScale.bandwidth()}
              fill="#ff00ff"
              
            />
          </Group>
        );
      })}
    </svg>
  );
}
export default BarGraph;