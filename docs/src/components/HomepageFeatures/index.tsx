import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: React.ReactElement;
};

const FeatureList: FeatureItem[] = [
  {
    title: '🐍 Pure Python',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Write your entire desktop application in <strong>pure Python</strong> - no JavaScript, HTML, or CSS required. 
        OneForAll handles the web technologies behind the scenes.
      </>
    ),
  },
  {
    title: '⚡ React-like Components',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Build UIs with familiar <strong>component-based architecture</strong>. Use built-in components like 
        <code>Text</code>, <code>Button</code>, and <code>Container</code> with reactive state management.
      </>
    ),
  },
  {
    title: '🎨 Tailwind CSS Integration',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Style your applications with <strong>Tailwind CSS utilities</strong> and enjoy hot reload during development. 
        Build modern, responsive desktop apps with ease.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): React.ReactElement {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
