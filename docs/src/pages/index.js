import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">Tasks Composer</h1>
        <p className="hero__subtitle">Gerencie suas tarefas de forma eficiente</p>
        <div className={styles.buttons}>
          <a
            className="button button--secondary button--lg"
            href="/Tasks-Composer-ADC/overview">
            Visão Geral do Projeto
          </a>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  return (
    <Layout
      title="Tasks Composer"
      description="Gerencie suas tarefas de forma eficiente e organizada">
      <HomepageHeader />
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              <div className="col col--4">
                <div className="text--center">
                  <img
                    src="/img/undraw_docusaurus_mountain.svg"
                    alt="Organização"
                    className={styles.featureImage}
                  />
                </div>
                <h3>Organização</h3>
                <p>Mantenha suas tarefas organizadas e nunca perca um prazo.</p>
              </div>
              <div className="col col--4">
                <div className="text--center">
                  <img
                    src="/img/undraw_docusaurus_tree.svg"
                    alt="Produtividade"
                    className={styles.featureImage}
                  />
                </div>
                <h3>Produtividade</h3>
                <p>Foque no que importa e aumente sua eficiência.</p>
              </div>
              <div className="col col--4">
                <div className="text--center">
                  <img
                    src="/img/undraw_docusaurus_react.svg"
                    alt="Simplicidade"
                    className={styles.featureImage}
                  />
                </div>
                <h3>Simplicidade</h3>
                <p>Uma interface intuitiva para facilitar seu dia a dia.</p>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
