import type {StructureResolver} from 'sanity/structure'

export const structure: StructureResolver = (S) =>
  S.list()
    .title('Maison Valér')
    .items([
      S.listItem().title('Site Settings').id('siteSettings')
        .child(S.document().schemaType('siteSettings').documentId('siteSettings')),
      S.listItem().title('Site Images').id('siteImages')
        .child(S.document().schemaType('siteImages').documentId('siteImages')),
      S.divider(),
      S.documentTypeListItem('category').title('Categories'),
      S.documentTypeListItem('product').title('Products'),
    ])
