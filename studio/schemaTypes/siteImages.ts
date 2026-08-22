import {defineType, defineField, defineArrayMember} from 'sanity'

const img = (name: string, title: string, desc: string, group: string) =>
  defineField({name, title, type: 'image', options: {hotspot: true}, description: desc, group})

export const siteImages = defineType({
  name: 'siteImages',
  title: 'Site Images',
  type: 'document',
  groups: [
    {name: 'home', title: 'Home', default: true},
    {name: 'about', title: 'About'},
    {name: 'other', title: 'Other / Future pages'},
  ],
  fields: [
    img('heroImage', 'Home — Hero banner',
        'Big banner at the top of the home page (also used as the social-share image). Landscape or square, at least 1600px wide. Keep the subject centred.', 'home'),
    img('homeFeature', 'Home — Desk-to-Destinations feature',
        'Square image (1:1), about 1200×1200px.', 'home'),
    img('homeImage1', 'Home — Section image 1 (landscape)',
        'Landscape, about 1100×880px (wider than tall).', 'home'),
    img('homeImage2', 'Home — Section image 2 (portrait)',
        'Portrait, about 1100×1470px (taller than wide).', 'home'),
    img('aboutImage1', 'About — Image 1 (landscape)',
        'Landscape, about 1500×1094px.', 'about'),
    img('aboutImage2', 'About — Image 2 (portrait)',
        'Portrait, about 950×1187px.', 'about'),
    defineField({
      name: 'extraImages',
      title: 'Extra images (for future pages)',
      type: 'array',
      group: 'other',
      description: 'Upload images here for new pages. Give each a "key" your developer will use to place it. Adding an image here does not put it on the site by itself — the developer wires the key into the new page.',
      of: [defineArrayMember({
        type: 'object', name: 'extraImage',
        fields: [
          defineField({name: 'key', title: 'Key (e.g. lookbook-hero)', type: 'string', validation: (r) => r.required()}),
          defineField({name: 'image', title: 'Image', type: 'image', options: {hotspot: true}}),
          defineField({name: 'note', title: 'Note (size / where it goes)', type: 'string'}),
        ],
        preview: {select: {title: 'key', media: 'image'}},
      })],
    }),
  ],
  preview: {prepare: () => ({title: 'Site Images'})},
})
