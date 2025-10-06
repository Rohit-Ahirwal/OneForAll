import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // OneForAll documentation sidebar with organized structure
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Tutorial - Basics',
      items: [
        'tutorial-basics/your-first-app',
        'tutorial-basics/components',
        'tutorial-basics/state-management',
        'tutorial-basics/creating-layouts',
        'tutorial-basics/styling',
        'tutorial-basics/multiple-windows',
      ],
    },
    {
      type: 'category',
      label: 'API Reference',
      items: [
        'api/app',
        'api/window',
        'api/components',
        'api/state-management',
        'api/cli',
      ],
    },
    'examples',
    {
      type: 'category',
      label: 'Advanced',
      items: [
        'advanced/custom-components',
      ],
    },
    {
      type: 'category',
      label: 'Deployment',
      items: [
        'deployment/building',
      ],
    },
  ],
};

export default sidebars;
