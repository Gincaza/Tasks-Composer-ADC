// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Tasks Composer',
  tagline: 'Gerencie suas tarefas de forma eficiente',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://github.com', // URL do GitHub Pages
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/Tasks-Composer-ADC/', // Caminho base do repositório

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Gincaza', // Nome do usuário ou organização no GitHub
  projectName: 'Tasks-Composer-ADC', // Nome do repositório no GitHub
  deploymentBranch: 'gh-pages', // <<< Adicionado aqui

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/', // Define a página inicial como a documentação
          editUrl: 'https://github.com/Gincaza/Tasks-Composer-ADC/edit/main/docs/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Tasks Composer',
        logo: {
          alt: 'Logo do Tasks Composer',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'overview',
            position: 'left',
            label: 'Visão Geral',
          },
          {
            href: 'https://github.com/Gincaza/Tasks-Composer-ADC',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Documentação',
            items: [
              {
                label: 'Visão Geral',
                to: '/',
              },
            ],
          },
          {
            title: 'Mais',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/Gincaza/Tasks-Composer-ADC',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Tasks Composer.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
