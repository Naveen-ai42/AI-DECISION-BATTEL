import { getCategoryConfig, getDefaultPrioritiesForCategory, CATEGORIES_CONFIG } from './src/config/categoryConfig.js';

console.log('Testing frontend category & subcategory configuration...\n');

const cases = [
  { cat: 'electronics', sub: 'laptop', expectedFirstAgent: 'Performance Agent', expectedRec: 'ASUS TUF Gaming A15' },
  { cat: 'electronics', sub: 'smartphone', expectedFirstAgent: 'Camera Agent', expectedRec: 'OnePlus 12R (5G)' },
  { cat: 'electronics', sub: 'smartwatch', expectedFirstAgent: 'Fitness & Health Agent', expectedRec: 'Garmin Forerunner 165' },
  { cat: 'finance', sub: '', expectedFirstAgent: 'Return Agent', expectedRec: 'Diversified Index & Flexi-Cap Allocation' },
  { cat: 'career', sub: '', expectedFirstAgent: 'Compensation Agent', expectedRec: 'Applied AI & ML Specialist Path' },
];

let allPassed = true;

for (const tc of cases) {
  const conf = getCategoryConfig(tc.cat, tc.sub);
  const prio = getDefaultPrioritiesForCategory(tc.cat, tc.sub);

  console.log(`Checking ${tc.cat}${tc.sub ? ' / ' + tc.sub : ''}:`);
  
  // Check factors count
  if (conf.factors.length !== 5) {
    console.error(`  FAIL: Expected 5 factors, got ${conf.factors.length}`);
    allPassed = false;
  } else {
    console.log(`  [OK] 5 factors: ${conf.factors.map(f => f.name).join(', ')}`);
  }

  // Check agents count and first agent
  if (conf.agents.length !== 5) {
    console.error(`  FAIL: Expected 5 agents, got ${conf.agents.length}`);
    allPassed = false;
  } else if (conf.agents[0].name !== tc.expectedFirstAgent) {
    console.error(`  FAIL: Expected first agent '${tc.expectedFirstAgent}', got '${conf.agents[0].name}'`);
    allPassed = false;
  } else {
    console.log(`  [OK] First agent matches: ${conf.agents[0].name}`);
  }

  // Check default recommendation
  if (conf.defaultRecommendation !== tc.expectedRec) {
    console.error(`  FAIL: Expected default rec '${tc.expectedRec}', got '${conf.defaultRecommendation}'`);
    allPassed = false;
  } else {
    console.log(`  [OK] Default recommendation: ${conf.defaultRecommendation}`);
  }

  // Check priorities sum to 100%
  const totalWeight = Object.values(prio).reduce((a, b) => a + b, 0);
  if (totalWeight !== 100) {
    console.error(`  FAIL: Priority sum is ${totalWeight}%, expected 100%`);
    allPassed = false;
  } else {
    console.log(`  [OK] Priority weights sum to 100%`);
  }

  console.log('');
}

if (allPassed) {
  console.log('ALL FRONTEND CATEGORY & SUBCATEGORY CONFIG TESTS PASSED!');
  process.exit(0);
} else {
  console.error('FRONTEND TESTS FAILED');
  process.exit(1);
}
