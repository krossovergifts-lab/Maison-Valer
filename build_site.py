# -*- coding: utf-8 -*-
"""Assemble Maison Valér static site — i18n (EN/RU/AR + RTL), gallery cards, no prices."""
import os, json

OUT = "site"
LANGS = ["en", "ru", "ar"]

# =====================================================================
# TRANSLATIONS  (key -> {en, ru, ar})
# =====================================================================
TR = {
 # chrome / nav
 "nav_home":       {"en":"Home","ru":"Главная","ar":"الرئيسية"},
 "nav_collection": {"en":"Collection","ru":"Коллекция","ar":"المجموعة"},
 "nav_d2d":        {"en":"Desk to Destinations","ru":"От стола до места назначения","ar":"من المكتب إلى الوجهة"},
 "nav_about":      {"en":"About","ru":"О нас","ar":"عن الدار"},
 "nav_contact":    {"en":"Contact","ru":"Контакты","ar":"اتصل بنا"},
 "cta_enquire":    {"en":"Enquire","ru":"Запрос","ar":"استفسار"},
 "lang_label":     {"en":"Language","ru":"Язык","ar":"اللغة"},
 "quick_look":     {"en":"Quick look","ru":"Быстрый просмотр","ar":"نظرة سريعة"},

 # colours
 "c_brown":{"en":"Brown","ru":"Коричневый","ar":"بنّي"},
 "c_black":{"en":"Black","ru":"Чёрный","ar":"أسود"},
 "c_gray": {"en":"Gray","ru":"Серый","ar":"رمادي"},
 "c_blue": {"en":"Blue","ru":"Синий","ar":"أزرق"},
 "c_green":{"en":"Green","ru":"Зелёный","ar":"أخضر"},

 # archetypes
 "arch_strategist":{"en":"The Strategist","ru":"Стратег","ar":"الاستراتيجي"},
 "arch_minimalist":{"en":"The Minimalist","ru":"Минималист","ar":"البسيط"},
 "arch_explorer":  {"en":"The Explorer","ru":"Исследователь","ar":"المستكشف"},
 "arch_identifier":{"en":"The Identifier","ru":"Идентификатор","ar":"المُعرّف"},
 "arch_companion": {"en":"The Companion","ru":"Компаньон","ar":"الرفيق"},
 "arch_reserve":   {"en":"The Reserve","ru":"Резерв","ar":"الاحتياطي"},
 "badge_new":      {"en":"New Arrival","ru":"Новинка","ar":"وصل حديثًا"},

 # products
 "p1_name":{"en":"Executive Organizer","ru":"Органайзер руководителя","ar":"منظّم تنفيذي"},
 "p1_sub": {"en":"with Magnetic Pen Holder","ru":"с магнитным держателем ручки","ar":"بحامل قلم مغناطيسي"},
 "p1_desc":{"en":"Notes, documents and a magnetic pen — held in one refined leather profile built for meetings and the move.",
            "ru":"Заметки, документы и магнитная ручка — в одном выверенном кожаном профиле для встреч и движения.",
            "ar":"ملاحظات ومستندات وقلم مغناطيسي — في هيكل جلدي أنيق مصمّم للاجتماعات والتنقّل."},
 "p2_name":{"en":"Magnetic Card Holder","ru":"Магнитный кардхолдер","ar":"حامل بطاقات مغناطيسي"},
 "p2_sub": {"en":"MagSafe Phone Wallet","ru":"Кошелёк MagSafe","ar":"محفظة هاتف ماغ‑سيف"},
 "p2_desc":{"en":"Everyday cards in a slim MagSafe form that snaps to the phone and disappears into the pocket.",
            "ru":"Повседневные карты в тонкой форме MagSafe, что крепится к телефону и исчезает в кармане.",
            "ar":"بطاقاتك اليومية في هيئة ماغ‑سيف نحيفة تلتصق بالهاتف وتختفي في الجيب."},
 "p3_name":{"en":"Premium Travel Wallet","ru":"Премиальный дорожный кошелёк","ar":"محفظة سفر فاخرة"},
 "p3_sub": {"en":"Multifunctional Passport Holder","ru":"Многофункциональная обложка для паспорта","ar":"حامل جواز متعدّد الوظائف"},
 "p3_desc":{"en":"Passport, cards and boarding pass in a structured fold — organised from check-in to destination.",
            "ru":"Паспорт, карты и посадочный талон в структурированном сложении — порядок от регистрации до места назначения.",
            "ar":"جواز السفر والبطاقات وبطاقة الصعود في طيّة منظّمة — ترتيب من تسجيل الوصول حتى الوجهة."},
 "p4_name":{"en":"Leather Luggage Tag","ru":"Кожаная багажная бирка","ar":"بطاقة حقائب جلدية"},
 "p4_sub": {"en":"Concealed ID","ru":"Скрытые данные","ar":"بيانات مخفية"},
 "p4_desc":{"en":"A quiet mark of ownership — refined presence on the belt, privacy for the details within.",
            "ru":"Тихий знак принадлежности — выверенное присутствие на ремне, приватность деталей внутри.",
            "ar":"علامة ملكية هادئة — حضور أنيق على الحزام وخصوصية للتفاصيل بالداخل."},
 "p5_name":{"en":"Magnetic Card Holder & Stand","ru":"Магнитный кардхолдер‑подставка","ar":"حامل بطاقات وحامل مغناطيسي"},
 "p5_sub": {"en":"Fold-out MagSafe Stand","ru":"Раскладная подставка MagSafe","ar":"حامل ماغ‑سيف قابل للطي"},
 "p5_desc":{"en":"Cards that hold, then fold — a magnetic stand for the desk, the flight, the in-between.",
            "ru":"Карты, что держат и складываются — магнитная подставка для стола, полёта, промежутка.",
            "ar":"بطاقات تُمسك ثم تُطوى — حامل مغناطيسي للمكتب والرحلة وما بينهما."},
 "p6_name":{"en":"Magnetic Power Bank & Stand","ru":"Магнитный павербанк‑подставка","ar":"بطارية وحامل مغناطيسي"},
 "p6_sub": {"en":"Wireless MagSafe Power","ru":"Беспроводная зарядка MagSafe","ar":"طاقة ماغ‑سيف لاسلكية"},
 "p6_desc":{"en":"Wireless power with a fold-out stand — a quiet reserve of energy that stays with the phone.",
            "ru":"Беспроводная энергия с раскладной подставкой — тихий резерв, что всегда с телефоном.",
            "ar":"طاقة لاسلكية مع حامل قابل للطي — احتياطي هادئ من الطاقة يبقى مع الهاتف."},

 # hero (home)
 "hero_eyebrow":{"en":"The Language of Considered Design","ru":"Язык продуманного дизайна","ar":"لغة التصميم المدروس"},
 "hero_title":  {"en":"Style,<br><em>refined.</em>","ru":"Стиль,<br><em>безупречный.</em>","ar":"أناقة<br><em>مُتقنة.</em>"},
 "hero_lede":   {"en":"Leather essentials for those who move between the desk and the world — refined in form, purposeful in function, consistent in character.",
                 "ru":"Кожаные аксессуары для тех, кто движется между рабочим столом и миром — выверенная форма, продуманная функция, постоянный характер.",
                 "ar":"إكسسوارات جلدية لمن ينتقلون بين المكتب والعالم — شكل مُنمّق، ووظيفة هادفة، وطابع ثابت."},
 "btn_explore": {"en":"Explore the collection","ru":"Смотреть коллекцию","ar":"استكشف المجموعة"},

 # ethos
 "house":     {"en":"The House","ru":"Дом","ar":"الدار"},
 "ethos_h":   {"en":"Design begins with <em>restraint.</em>","ru":"Дизайн начинается со <em>сдержанности.</em>","ar":"يبدأ التصميم بـ<em>الاعتدال.</em>"},
 "ethos_lede":{"en":"Each detail is deliberate, each material chosen for its integrity, each form shaped to serve a clear purpose. The result is a collection that speaks through clarity — not noise.",
               "ru":"Каждая деталь продумана, каждый материал выбран за его качество, каждая форма служит ясной цели. Результат — коллекция, говорящая ясностью, а не шумом.",
               "ar":"كل تفصيل مقصود، وكل خامة مختارة لجودتها، وكل شكل مصمّم لغرض واضح. والنتيجة مجموعة تتحدّث بالوضوح لا بالضجيج."},
 "stat_pieces":  {"en":"Signature pieces","ru":"Фирменные изделия","ar":"قطع مميّزة"},
 "stat_finishes":{"en":"Leather finishes","ru":"Виды отделки","ar":"تشطيبات جلدية"},
 "stat_idea":    {"en":"Considered idea","ru":"Продуманная идея","ar":"فكرة مدروسة"},
 "read_philosophy":{"en":"Read our philosophy","ru":"Наша философия","ar":"اقرأ فلسفتنا"},

 # collection preview
 "coll_label":    {"en":"The Collection","ru":"Коллекция","ar":"المجموعة"},
 "coll_prev_h":   {"en":"Essentials, edited.","ru":"Аксессуары, выверенные.","ar":"أساسيات مُنتقاة."},
 "coll_prev_lede":{"en":"Four archetypes for the working professional — and the accessories that keep them powered and in place.",
                   "ru":"Четыре архетипа для профессионала — и аксессуары, что держат их заряженными и на месте.",
                   "ar":"أربعة نماذج للمحترف العامل — والإكسسوارات التي تبقيه مشحونًا ومنظّمًا."},
 "view_all":      {"en":"View all six pieces","ru":"Все шесть изделий","ar":"اعرض القطع الست"},

 # d2d band + materials (home)
 "featured_theme":{"en":"Featured Theme","ru":"Избранная тема","ar":"الموضوع المميّز"},
 "d2d_band_h":    {"en":"Desk to <em>Destination.</em>","ru":"От стола до <em>назначения.</em>","ar":"من المكتب إلى <em>الوجهة.</em>"},
 "d2d_band_lede": {"en":"A curated leather family for professionals who value order, movement and presence. Each piece transitions seamlessly between work and travel — not accessories, but companions.",
                   "ru":"Продуманная кожаная семья для профессионалов, ценящих порядок, движение и присутствие. Каждое изделие легко переходит от работы к путешествию — не аксессуары, а спутники.",
                   "ar":"عائلة جلدية مُنسّقة للمحترفين الذين يقدّرون النظام والحركة والحضور. تنتقل كل قطعة بسلاسة بين العمل والسفر — ليست إكسسوارات، بل رفاق."},
 "meet_family":   {"en":"Meet the family","ru":"Познакомиться","ar":"تعرّف على العائلة"},
 "materials":     {"en":"Materials","ru":"Материалы","ar":"الخامات"},
 "materials_h":   {"en":"Selected for <em>longevity.</em>","ru":"Выбрано для <em>долговечности.</em>","ar":"مُختارة لـ<em>المتانة.</em>"},
 "materials_lede":{"en":"Material, form and finish in perfect balance. Premium leather that ages naturally, stitching built for daily use, and a branding-ready surface made for the mark that matters — yours.",
                   "ru":"Материал, форма и отделка в идеальном балансе. Премиальная кожа, что стареет естественно, прошивка для ежедневного использования и поверхность, готовая к брендингу — для вашего знака.",
                   "ar":"خامة وشكل وتشطيب في توازن تام. جلد فاخر يتقادم بطبيعته، وخياطة تتحمّل الاستخدام اليومي، وسطح جاهز للعلامة الذي يهمّ — علامتك."},
 "mat1_h":{"en":"Full-grain leather","ru":"Цельнозернистая кожа","ar":"جلد كامل الحبيبات"},
 "mat1_p":{"en":"Chosen for integrity and a patina that deepens with time.","ru":"Выбрана за качество и патину, что углубляется со временем.","ar":"مُختار لجودته ولبريقٍ يزداد عمقًا مع الوقت."},
 "mat2_h":{"en":"Made to be marked","ru":"Создано для вашего знака","ar":"صُنع ليحمل علامتك"},
 "mat2_p":{"en":"A clean, considered surface for embossed or foiled identity.","ru":"Чистая, продуманная поверхность для тиснёной идентичности.","ar":"سطح نظيف ومدروس لهويّة مطبوعة أو مذهّبة."},

 # collection page
 "coll_2026":{"en":"The Collection · 2026","ru":"Коллекция · 2026","ar":"المجموعة · 2026"},
 "coll_h":   {"en":"Six pieces,<br>one <em>standard.</em>","ru":"Шесть изделий,<br>один <em>стандарт.</em>","ar":"ست قطع،<br>معيار <em>واحد.</em>"},
 "coll_lede":{"en":"Every item is offered in a considered range of finishes and made ready for your brand.",
              "ru":"Каждое изделие предлагается в продуманной гамме отделок и готово к вашему бренду.",
              "ar":"تُقدّم كل قطعة بمجموعة مدروسة من التشطيبات وجاهزة لعلامتك التجارية."},
 "filter_all":     {"en":"All","ru":"Все","ar":"الكل"},
 "filter_desk":    {"en":"Desk","ru":"Стол","ar":"المكتب"},
 "filter_travel":  {"en":"Travel","ru":"Путешествия","ar":"السفر"},
 "filter_everyday":{"en":"Everyday","ru":"Каждый день","ar":"اليومي"},
 "filter_gifting": {"en":"Gifting","ru":"Подарки","ar":"الهدايا"},

 # feature strip
 "feat1_h":{"en":"Premium Leather","ru":"Премиальная кожа","ar":"جلد فاخر"},
 "feat1_p":{"en":"Full-grain construction with a refined, natural texture.","ru":"Цельнозернистая конструкция с выверенной естественной текстурой.","ar":"بناء كامل الحبيبات بملمس طبيعي أنيق."},
 "feat2_h":{"en":"Magnetic Detail","ru":"Магнитная деталь","ar":"تفصيل مغناطيسي"},
 "feat2_p":{"en":"Considered magnetic closures and MagSafe alignment.","ru":"Продуманные магнитные застёжки и выравнивание MagSafe.","ar":"إغلاقات مغناطيسية مدروسة ومحاذاة ماغ‑سيف."},
 "feat3_h":{"en":"Slim Profile","ru":"Тонкий профиль","ar":"هيكل نحيف"},
 "feat3_p":{"en":"Executive forms that slip into bag, pocket or briefcase.","ru":"Формы, что скользят в сумку, карман или портфель.","ar":"تصاميم تنزلق في الحقيبة أو الجيب أو حقيبة العمل."},
 "feat4_h":{"en":"Branding Ready","ru":"Готово к брендингу","ar":"جاهز للعلامة"},
 "feat4_p":{"en":"A clean surface built for embossed or foiled identity.","ru":"Чистая поверхность для тиснёной идентичности.","ar":"سطح نظيف مهيّأ لهويّة مطبوعة أو مذهّبة."},
 "feat5_h":{"en":"Gift Ready","ru":"Готово к подарку","ar":"جاهز للإهداء"},
 "feat5_p":{"en":"Corporate-gifting presentation, out of the box.","ru":"Презентация корпоративного подарка из коробки.","ar":"عرض هدايا مؤسسية جاهز من العلبة."},

 # d2d page
 "d2d_title":{"en":"Desk to<br><em>destination.</em>","ru":"От стола<br>до <em>назначения.</em>","ar":"من المكتب<br>إلى <em>الوجهة.</em>"},
 "d2d_lede": {"en":"A curated leather essentials theme for professionals who value order, movement and presence — crafted to transition seamlessly between work and travel.",
              "ru":"Продуманная кожаная тема для профессионалов, ценящих порядок, движение и присутствие — создана для лёгкого перехода между работой и путешествием.",
              "ar":"موضوع إكسسوارات جلدية مُنسّق للمحترفين الذين يقدّرون النظام والحركة والحضور — صُمّم للانتقال بسلاسة بين العمل والسفر."},
 "the_idea":     {"en":"The Idea","ru":"Идея","ar":"الفكرة"},
 "idea_manifesto":{"en":"Not accessories. <em>Companions</em> — built to carry ideas, identity and intent.",
                   "ru":"Не аксессуары. <em>Спутники</em> — созданы нести идеи, идентичность и намерение.",
                   "ar":"ليست إكسسوارات. <em>رفاق</em> — صُنعوا لحمل الأفكار والهوية والقصد."},
 "meta_bestfor":{"en":"Best for","ru":"Лучше всего для","ar":"الأنسب لـ"},
 "meta_carries":{"en":"Carries","ru":"Вмещает","ar":"يحمل"},
 "a1_p":{"en":"Perfect for meetings, planning sessions and executive gifting. Keeps ideas, tools and workflow aligned — whether at the desk or on the move.",
         "ru":"Идеален для встреч, планирования и корпоративных подарков. Держит идеи, инструменты и процессы вместе — за столом или в движении.",
         "ar":"مثالي للاجتماعات وجلسات التخطيط والإهداء التنفيذي. يُبقي الأفكار والأدوات وسير العمل منظّمًا — على المكتب أو أثناء التنقّل."},
 "a1_use":{"en":"Meetings · Travel work","ru":"Встречи · Работа в пути","ar":"اجتماعات · عمل السفر"},
 "a1_carry":{"en":"Notes · Pen · Documents","ru":"Заметки · Ручка · Документы","ar":"ملاحظات · قلم · مستندات"},
 "a2_p":{"en":"Ideal for everyday professionals who prefer lightweight carry. Seamlessly transitions from office use to travel without the need for a full wallet.",
         "ru":"Идеален для тех, кто предпочитает лёгкость. Легко переходит от офиса к путешествию без полноценного кошелька.",
         "ar":"مثالي للمحترفين الذين يفضّلون الحمل الخفيف. ينتقل بسلاسة من المكتب إلى السفر دون الحاجة لمحفظة كاملة."},
 "a2_use":{"en":"Everyday · Commute","ru":"Каждый день · Дорога","ar":"يومي · تنقّل"},
 "a2_carry":{"en":"Cards · MagSafe","ru":"Карты · MagSafe","ar":"بطاقات · ماغ‑سيف"},
 "a3_p":{"en":"Designed for frequent travellers, executives and corporate gifting. Keeps travel essentials organised and accessible from check-in to destination.",
         "ru":"Создан для частых путешественников, руководителей и корпоративных подарков. Держит дорожные вещи в порядке от регистрации до места назначения.",
         "ar":"مُصمّم للمسافرين الدائمين والتنفيذيين والإهداء المؤسسي. يُبقي أساسيات السفر منظّمة ومتاحة من تسجيل الوصول حتى الوجهة."},
 "a3_use":{"en":"Travel · Business","ru":"Путешествия · Бизнес","ar":"سفر · أعمال"},
 "a3_carry":{"en":"Passport · Cards · Pass","ru":"Паспорт · Карты · Талон","ar":"جواز · بطاقات · تصريح"},
 "a4_p":{"en":"Ideal for business travel, corporate gifting and brand identity. Adds a refined, professional presence while ensuring easy luggage recognition.",
         "ru":"Идеален для деловых поездок, корпоративных подарков и айдентики. Добавляет выверенное присутствие и облегчает узнавание багажа.",
         "ar":"مثالي لسفر الأعمال والإهداء المؤسسي وهوية العلامة. يضيف حضورًا أنيقًا مع تسهيل تمييز الأمتعة."},
 "a4_use":{"en":"Travel · Gifting","ru":"Путешествия · Подарки","ar":"سفر · هدايا"},
 "a4_carry":{"en":"Concealed ID","ru":"Скрытые данные","ar":"بيانات مخفية"},

 # about
 "about_h":{"en":"Clarity,<br>not <em>noise.</em>","ru":"Ясность,<br>не <em>шум.</em>","ar":"وضوح،<br>لا <em>ضجيج.</em>"},
 "about_manifesto":{"en":"Every detail serves a <em>purpose</em> — material, form and finish in perfect balance.",
                    "ru":"Каждая деталь служит <em>цели</em> — материал, форма и отделка в идеальном балансе.",
                    "ar":"كل تفصيل يخدم <em>غرضًا</em> — خامة وشكل وتشطيب في توازن تام."},
 "about_p1":{"en":"Maison Valér is designed for those who value precision, restraint and timeless clarity. Design begins with restraint: each detail deliberate, each material chosen for its integrity, and each form shaped to serve a clear purpose.",
             "ru":"Maison Valér создан для тех, кто ценит точность, сдержанность и вневременную ясность. Дизайн начинается со сдержанности: каждая деталь продумана, каждый материал выбран за качество, каждая форма служит ясной цели.",
             "ar":"صُمّمت ميزون فاليّر لمن يقدّرون الدقّة والاعتدال والوضوح الخالد. يبدأ التصميم بالاعتدال: كل تفصيل مقصود، وكل خامة مختارة لجودتها، وكل شكل مصمّم لغرض واضح."},
 "about_p2":{"en":"The result is a collection that speaks through clarity — a considered response to a world that too often shouts. We prefer to brand smarter, not louder.",
             "ru":"Результат — коллекция, говорящая ясностью, — продуманный ответ миру, что слишком часто кричит. Мы предпочитаем брендировать умнее, а не громче.",
             "ar":"والنتيجة مجموعة تتحدّث بالوضوح — ردّ مدروس على عالم كثيرًا ما يصرخ. نحن نفضّل العلامة الأذكى لا الأعلى صوتًا."},
 "principles":  {"en":"Principles","ru":"Принципы","ar":"المبادئ"},
 "principles_h":{"en":"What we hold to.","ru":"Чего мы держимся.","ar":"ما نلتزم به."},
 "pr1_h":{"en":"Restraint","ru":"Сдержанность","ar":"الاعتدال"},
 "pr1_p":{"en":"We remove before we add. Nothing on a Maison Valér piece is there to decorate — only to serve.",
          "ru":"Мы убираем прежде, чем добавить. Ничто в изделии Maison Valér не украшает — только служит.",
          "ar":"نحذف قبل أن نضيف. لا شيء في قطعة ميزون فاليّر للزينة — بل للخدمة فقط."},
 "pr2_h":{"en":"Integrity","ru":"Целостность","ar":"الجودة"},
 "pr2_p":{"en":"Materials are selected for longevity. Full-grain leather that ages honestly, stitching built for daily use.",
          "ru":"Материалы выбраны для долговечности. Цельнозернистая кожа, что стареет честно, прошивка для ежедневного использования.",
          "ar":"تُختار الخامات للمتانة. جلد كامل الحبيبات يتقادم بصدق، وخياطة تتحمّل الاستخدام اليومي."},
 "pr3_h":{"en":"Presence","ru":"Присутствие","ar":"الحضور"},
 "pr3_p":{"en":"Refined form that carries identity quietly — a considered surface made ready for your mark.",
          "ru":"Выверенная форма, что тихо несёт идентичность — продуманная поверхность, готовая к вашему знаку.",
          "ar":"شكل أنيق يحمل الهوية بهدوء — سطح مدروس جاهز لعلامتك."},
 "fdd":  {"en":"From desk to destination","ru":"От стола до места назначения","ar":"من المكتب إلى الوجهة"},
 "fdd_h":{"en":"Built to <em>move</em> with you.","ru":"Создано <em>двигаться</em> с вами.","ar":"صُنع لـ<em>يتحرّك</em> معك."},
 "fdd_lede":{"en":"Our essentials are made for professionals in motion — the organiser on the desk, the card holder in the pocket, the passport wallet at the gate, the tag on the case. One consistent character, wherever work takes you.",
             "ru":"Наши аксессуары созданы для профессионалов в движении — органайзер на столе, кардхолдер в кармане, обложка паспорта у выхода, бирка на чемодане. Один постоянный характер, куда бы ни привела работа.",
             "ar":"صُنعت أساسياتنا للمحترفين في حركة — المنظّم على المكتب، وحامل البطاقات في الجيب، ومحفظة الجواز عند البوابة، والبطاقة على الحقيبة. طابع واحد ثابت أينما أخذك العمل."},
 "explore_theme":{"en":"Explore the theme","ru":"Смотреть тему","ar":"استكشف الموضوع"},

 # contact
 "enquire_label":{"en":"Enquire","ru":"Запрос","ar":"استفسار"},
 "contact_h":{"en":"Let's make it <em>yours.</em>","ru":"Сделаем его <em>вашим.</em>","ar":"لنجعله <em>لك.</em>"},
 "contact_lede":{"en":"Tell us about your brand and the occasion. We'll come back with finishes, branding options and lead times for corporate gifting, wholesale or bespoke runs.",
                 "ru":"Расскажите о вашем бренде и поводе. Мы вернёмся с отделками, вариантами брендинга и сроками для корпоративных подарков, опта или индивидуальных партий.",
                 "ar":"أخبرنا عن علامتك والمناسبة. سنعود إليك بالتشطيبات وخيارات العلامة ومُدد التنفيذ للإهداء المؤسسي أو الجملة أو الطلبات الخاصة."},
 "c_email":{"en":"Email","ru":"Эл. почта","ar":"البريد الإلكتروني"},
 "c_studio":{"en":"Studio","ru":"Студия","ar":"الاستوديو"},
 "c_studio_v":{"en":"Dubai · United Arab Emirates","ru":"Дубай · ОАЭ","ar":"دبي · الإمارات العربية المتحدة"},
 "c_trade":{"en":"Trade","ru":"Опт","ar":"التجارة"},
 "c_trade_v":{"en":"Wholesale & corporate gifting","ru":"Опт и корпоративные подарки","ar":"الجملة والإهداء المؤسسي"},
 "f_name":{"en":"Name","ru":"Имя","ar":"الاسم"},
 "f_email":{"en":"Email","ru":"Эл. почта","ar":"البريد الإلكتروني"},
 "f_company":{"en":"Company","ru":"Компания","ar":"الشركة"},
 "f_quantity":{"en":"Quantity","ru":"Количество","ar":"الكمية"},
 "f_interest":{"en":"Piece of interest","ru":"Интересующее изделие","ar":"القطعة المهتمّ بها"},
 "f_message":{"en":"Message","ru":"Сообщение","ar":"الرسالة"},
 "ph_name":{"en":"Your name","ru":"Ваше имя","ar":"اسمك"},
 "ph_company":{"en":"Company / brand","ru":"Компания / бренд","ar":"الشركة / العلامة"},
 "ph_quantity":{"en":"e.g. 250 units","ru":"напр. 250 шт.","ar":"مثال: 250 قطعة"},
 "ph_message":{"en":"Tell us about the occasion, branding and timeline…","ru":"Расскажите о поводе, брендинге и сроках…","ar":"أخبرنا عن المناسبة والعلامة والجدول الزمني…"},
 "opt_full":{"en":"The full collection","ru":"Вся коллекция","ar":"المجموعة الكاملة"},
 "opt_d2d":{"en":"Desk to Destinations set","ru":"Набор Desk to Destinations","ar":"طقم من المكتب إلى الوجهة"},
 "opt_bespoke":{"en":"Bespoke / other","ru":"Индивидуально / другое","ar":"حسب الطلب / أخرى"},
 "btn_send":{"en":"Send enquiry","ru":"Отправить запрос","ar":"إرسال الاستفسار"},
 "form_note":{"en":"This opens your email client with the details prefilled. Prefer to write directly?",
              "ru":"Откроется почтовый клиент с заполненными данными. Хотите написать напрямую?",
              "ar":"سيفتح هذا برنامج بريدك مع تعبئة التفاصيل. تفضّل المراسلة مباشرة؟"},

 # footer + cta
 "cta_eyebrow":{"en":"Corporate gifting · Wholesale · Bespoke","ru":"Корпоративные подарки · Опт · Индивидуально","ar":"إهداء مؤسسي · جملة · حسب الطلب"},
 "cta_h":{"en":"Carry something <em>considered.</em>","ru":"Носите нечто <em>продуманное.</em>","ar":"احمل شيئًا <em>مدروسًا.</em>"},
 "cta_lede":{"en":"Maison Valér partners with brands and businesses to craft leather essentials that carry identity, intent, and lasting impression — from a single desk to a thousand.",
             "ru":"Maison Valér сотрудничает с брендами и компаниями, создавая кожаные аксессуары, что несут идентичность, намерение и стойкое впечатление — от одного стола до тысячи.",
             "ar":"تتعاون ميزون فاليّر مع العلامات والشركات لصناعة إكسسوارات جلدية تحمل الهوية والقصد والانطباع الدائم — من مكتب واحد إلى ألف."},
 "start_enquiry":{"en":"Start an enquiry","ru":"Начать запрос","ar":"ابدأ استفسارًا"},
 "foot_brand_desc":{"en":"Leather essentials shaped for professionals who move between the desk and the world. Refined in form, purposeful in function.",
                    "ru":"Кожаные аксессуары для профессионалов, что движутся между столом и миром. Выверенная форма, продуманная функция.",
                    "ar":"إكسسوارات جلدية للمحترفين الذين ينتقلون بين المكتب والعالم. شكل مُنمّق ووظيفة هادفة."},
 "foot_explore":{"en":"Explore","ru":"Обзор","ar":"استكشف"},
 "foot_collection":{"en":"Collection","ru":"Коллекция","ar":"المجموعة"},
 "foot_connect":{"en":"Connect","ru":"Связь","ar":"تواصل"},
 "foot_the_collection":{"en":"The Collection","ru":"Коллекция","ar":"المجموعة"},
 "foot_the_house":{"en":"The House","ru":"Дом","ar":"الدار"},
 "foot_trade":{"en":"Trade & Wholesale","ru":"Опт и торговля","ar":"التجارة والجملة"},
 "foot_tagline":{"en":"The language of considered design.","ru":"Язык продуманного дизайна.","ar":"لغة التصميم المدروس."},
 "foot_style":{"en":"Style, Refined.","ru":"Стиль. Безупречно.","ar":"أناقة مُتقنة."},
}

def EN(k):  return TR[k]["en"]
def A(k):   return f'data-i18n="{k}"'
def AH(k):  return f'data-i18n-html="{k}"'

# =====================================================================
# SVG icons
# =====================================================================
ARW  = '<svg class="arw" viewBox="0 0 24 24" fill="none" width="16" height="16" aria-hidden="true"><path d="M4 12h15m0 0-6-6m6 6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SUN  = '<svg class="i-sun" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.5"/><path d="M12 2.5v2.6M12 18.9v2.6M4.2 4.2l1.9 1.9M17.9 17.9l1.9 1.9M2.5 12h2.6M18.9 12h2.6M4.2 19.8l1.9-1.9M17.9 6.1l1.9-1.9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
MOON = '<svg class="i-moon" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>'
IC_LEATHER='<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><path d="M16 4c3 3 7 3 10 2-1 4-1 7 1 10-3 1-5 3-6 6-2-2-5-2-7 0-1-3-3-5-6-6 2-3 2-6 1-10 3 1 7 1 12-2Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M16 10v9" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="1 3"/></svg>'
IC_PEN='<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="14" y="5" width="4" height="22" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M9 11c-2 1.7-2 8.3 0 10M23 11c2 1.7 2 8.3 0 10" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>'
IC_SLIM='<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="7" y="5" width="18" height="22" rx="2.5" stroke="currentColor" stroke-width="1.4"/><path d="M11 5v22" stroke="currentColor" stroke-width="1.4"/><path d="M18 14h4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>'
IC_BRAND='<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="5" y="8" width="22" height="16" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M24 6l2 2M22 8l3-3 2 2-3 3" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>'
IC_GIFT='<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="6" y="13" width="20" height="13" rx="1.5" stroke="currentColor" stroke-width="1.4"/><path d="M4 13h24v4H4zM16 13v13" stroke="currentColor" stroke-width="1.4"/><path d="M16 13c-4 0-6-1-6-3.5S12 6 16 13Zm0 0c4 0 6-1 6-3.5S20 6 16 13Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>'
MONO = '<span class="mono" aria-hidden="true"></span>'

def wordmark():
    return ('<span class="wordmark"><span class="maison">Maison</span>'
            '<span class="valer">Valér</span></span>')

def lang_switch(cls=""):
    btns = "".join(
        f'<button type="button" data-lang="{L}"{" class=\"active\"" if L=="en" else ""}>{lab}</button>'
        for L, lab in [("en","EN"),("ru","RU"),("ar","ع")])
    return f'<div class="lang-switch {cls}" role="group" aria-label="{EN("lang_label")}">{btns}</div>'

# =====================================================================
# Head / Header / Footer
# =====================================================================
def head(title, desc, page):
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#14100c">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="preload" href="fonts/fraunces-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
<script src="js/i18n.js"></script>
</head>
<body>'''

NAV_ITEMS = [
    ("index.html", "nav_home", "home"),
    ("collection.html", "nav_collection", "collection"),
    ("desk-to-destinations.html", "nav_d2d", "d2d"),
    ("about.html", "nav_about", "about"),
    ("contact.html", "nav_contact", "contact"),
]

def header(page):
    links = ""
    for href, key, k in NAV_ITEMS:
        cur = ' aria-current="page"' if k == page else ""
        links += f'<a href="{href}"{cur} {A(key)}>{EN(key)}</a>'
    draw = ""
    for i, (href, key, k) in enumerate(NAV_ITEMS, 1):
        draw += f'<a href="{href}"><span class="n">0{i}</span><span {A(key)}>{EN(key)}</span></a>'
    over = " over-dark" if page in ("home", "d2d") else ""
    return f'''
<header class="site-head{over}">
  <div class="head-inner">
    <a class="brand" href="index.html" aria-label="Maison Valér home">{MONO}{wordmark()}</a>
    <nav class="nav" aria-label="Primary">{links}</nav>
    <div class="head-actions">
      {lang_switch()}
      <button class="theme-toggle" type="button" aria-label="Switch colour theme">{SUN}{MOON}</button>
      <a class="btn btn--solid head-cta" href="contact.html"><span {A("cta_enquire")}>{EN("cta_enquire")}</span> {ARW}</a>
      <button class="burger" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<nav class="drawer" aria-label="Mobile">{draw}{lang_switch("in-drawer")}</nav>
<div class="side-rail" aria-hidden="true">#MaisonValér — Style, Refined</div>
'''

def MONO_BIG():
    return '<span class="mono" aria-hidden="true" style="width:clamp(160px,30vw,340px);height:clamp(160px,30vw,340px);color:var(--bone);opacity:.05;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:0"></span>'

def footer():
    return f'''
<section class="section cta-band">
  {MONO_BIG()}
  <div class="wrap reveal">
    <p class="eyebrow center" style="justify-content:center" {A("cta_eyebrow")}>{EN("cta_eyebrow")}</p>
    <h2 class="display" style="margin-top:22px" {AH("cta_h")}>{TR["cta_h"]["en"]}</h2>
    <p class="lede" {A("cta_lede")}>{EN("cta_lede")}</p>
    <a class="btn btn--solid" href="contact.html"><span {A("start_enquiry")}>{EN("start_enquiry")}</span> {ARW}</a>
  </div>
</section>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        {MONO}
        {wordmark()}
        <p {A("foot_brand_desc")}>{EN("foot_brand_desc")}</p>
      </div>
      <div class="foot-col">
        <h5 {A("foot_explore")}>{EN("foot_explore")}</h5>
        <a href="collection.html" {A("foot_the_collection")}>{EN("foot_the_collection")}</a>
        <a href="desk-to-destinations.html" {A("nav_d2d")}>{EN("nav_d2d")}</a>
        <a href="about.html" {A("foot_the_house")}>{EN("foot_the_house")}</a>
        <a href="contact.html" {A("cta_enquire")}>{EN("cta_enquire")}</a>
      </div>
      <div class="foot-col">
        <h5 {A("foot_collection")}>{EN("foot_collection")}</h5>
        <a href="collection.html" {A("arch_strategist")}>{EN("arch_strategist")}</a>
        <a href="collection.html" {A("arch_minimalist")}>{EN("arch_minimalist")}</a>
        <a href="collection.html" {A("arch_explorer")}>{EN("arch_explorer")}</a>
        <a href="collection.html" {A("arch_identifier")}>{EN("arch_identifier")}</a>
      </div>
      <div class="foot-col">
        <h5 {A("foot_connect")}>{EN("foot_connect")}</h5>
        <a href="mailto:hello@maisonvaler.com">hello@maisonvaler.com</a>
        <a href="contact.html" {A("c_studio_v")}>{EN("c_studio_v")}</a>
        <a href="contact.html" {A("foot_trade")}>{EN("foot_trade")}</a>
      </div>
    </div>
    <div class="foot-bottom">
      <p>© <span data-year>2026</span> Maison Valér. <span {A("foot_tagline")}>{EN("foot_tagline")}</span></p>
      <p {A("foot_style")}>{EN("foot_style")}</p>
    </div>
  </div>
</footer>
<script src="js/site.js"></script>
</body>
</html>'''

# =====================================================================
# Products
# =====================================================================
PRODUCTS = [
 dict(key="p1", sku="REXORA-11653", arch="strategist", cat="desk gifting",
      colors=[("brown",["organizer-brown-1","organizer-brown-2","organizer-brown-3"]),
              ("black",["organizer-black-1","organizer-black-2"]),
              ("gray", ["organizer-gray-1","organizer-gray-2"])]),
 dict(key="p2", sku="MAGTEC-11659", arch="minimalist", cat="travel everyday",
      colors=[("brown",["cardholder-brown-1","cardholder-brown-2"]),
              ("black",["cardholder-black-1"]),
              ("gray", ["cardholder-gray-1"])]),
 dict(key="p3", sku="LEPORT-11662", arch="explorer", cat="travel gifting",
      colors=[("brown",["travelwallet-brown-1","travelwallet-brown-2"]),
              ("black",["travelwallet-black-1"]),
              ("gray", ["travelwallet-gray-1"])]),
 dict(key="p4", sku="LETHEG-11658", arch="identifier", cat="travel gifting",
      colors=[("brown",["luggagetag-brown-1","luggagetag-brown-2"]),
              ("black",["luggagetag-black-1"]),
              ("gray", ["luggagetag-gray-1"])]),
 dict(key="p5", sku="MAGFOLD-11656", arch="companion", cat="everyday desk",
      colors=[("gray", ["foldstand-gray-1","foldstand-gray-2"]),
              ("blue", ["foldstand-blue-1"]),
              ("green",["foldstand-green-1"])]),
 dict(key="p6", sku="MAGFOLDRA-11655", arch="reserve", cat="everyday desk",
      colors=[("blue", ["powerbank-blue-1","powerbank-blue-2"]),
              ("gray", ["powerbank-gray-1"])]),
]

def swatch_buttons(p):
    s = ""
    for i, (c, _imgs) in enumerate(p["colors"]):
        active = " active" if i == 0 else ""
        s += (f'<button type="button" class="swatch sw-{c}{active}" data-color="{c}" '
              f'data-i18n-title="c_{c}" title="{EN("c_"+c)}" aria-label="{EN("c_"+c)}"></button>')
    return f'<div class="swatches" role="group" aria-label="Colour">{s}</div>'

def product_card(p, delay=""):
    colors_json = [{"k": c, "name": EN("c_"+c), "imgs": imgs} for c, imgs in p["colors"]]
    data = json.dumps({"colors": colors_json}, ensure_ascii=False).replace("</", "<\\/")
    first = p["colors"][0][1][0]
    namekey = p["key"] + "_name"; subkey = p["key"] + "_sub"; desckey = p["key"] + "_desc"
    return f'''
      <article class="pcard reveal {delay}" data-cat="{p['cat']}">
        <div class="pcard-media">
          <span class="pcard-tag" {A("badge_new")}>{EN("badge_new")}</span>
          <span class="pcard-arch" {A("arch_"+p['arch'])}>{EN("arch_"+p['arch'])}</span>
          <a class="pcard-link" href="collection.html" aria-label="{EN(namekey)}" data-i18n-aria="quick_look">
            <img class="pcard-img" src="images/products/{first}.webp" alt="{EN(namekey)}" loading="lazy" width="1200" height="1200">
          </a>
          <div class="pcard-thumbs" aria-hidden="true"></div>
        </div>
        <div class="pcard-body">
          <span class="sku">{p['sku']}</span>
          <h3><span {A(namekey)}>{EN(namekey)}</span><br><span class="sub" {A(subkey)}>{EN(subkey)}</span></h3>
          <p {A(desckey)}>{EN(desckey)}</p>
          <div class="pcard-foot">{swatch_buttons(p)}</div>
        </div>
        <script type="application/json" class="pcard-json">{data}</script>
      </article>'''

def feature_strip():
    feats = [(IC_LEATHER,"feat1"),(IC_PEN,"feat2"),(IC_SLIM,"feat3"),(IC_BRAND,"feat4"),(IC_GIFT,"feat5")]
    inner = "".join(
        f'<div class="feat">{ic}<h4 {A(k+"_h")}>{EN(k+"_h")}</h4><p {A(k+"_p")}>{EN(k+"_p")}</p></div>'
        for ic,k in feats)
    return f'''
  <section class="section--tight">
    <div class="feat-strip reveal">{inner}</div>
  </section>'''

# =====================================================================
# PAGE: HOME
# =====================================================================
def page_home():
    cards = "".join(product_card(p, ["","d1","d2","d3"][i]) for i, p in enumerate(PRODUCTS[:3]))
    return head("Maison Valér — Style, Refined.",
                "Maison Valér crafts premium leather essentials for work, travel and executive gifting. The language of considered design.",
                "home") + header("home") + f'''
<main>
  <section class="hero">
    <div class="hero-media" data-parallax="0.12">
      <img src="images/hero-desk.webp" alt="Maison Valér cognac leather desk essentials" width="1900" height="1900" fetchpriority="high">
    </div>
    <div class="hero-inner wrap">
      <p class="hero-eyebrow eyebrow fade-seq d1" {A("hero_eyebrow")}>{EN("hero_eyebrow")}</p>
      <h1 class="hero-title display" {AH("hero_title")}>{TR["hero_title"]["en"]}</h1>
      <div class="hero-sub fade-seq d2">
        <p class="lede" {A("hero_lede")}>{EN("hero_lede")}</p>
        <div style="display:flex;gap:14px;flex-wrap:wrap;align-items:center">
          <a class="btn btn--solid" href="collection.html"><span {A("btn_explore")}>{EN("btn_explore")}</span> {ARW}</a>
          <a class="btn btn--ghost" href="desk-to-destinations.html" {A("nav_d2d")}>{EN("nav_d2d")}</a>
        </div>
      </div>
    </div>
  </section>

  <div class="ribbon" aria-hidden="true">
    <div class="ribbon-track">
      <span>Style, Refined.</span><span class="star">✦</span>
      <span>The Language of Considered Design</span><span class="star">✦</span>
      <span>Brand Smarter, Not Louder</span><span class="star">✦</span>
      <span>Desk to Destination</span><span class="star">✦</span>
      <span>Style, Refined.</span><span class="star">✦</span>
      <span>The Language of Considered Design</span><span class="star">✦</span>
      <span>Brand Smarter, Not Louder</span><span class="star">✦</span>
      <span>Desk to Destination</span><span class="star">✦</span>
    </div>
  </div>

  <section class="section ethos">
    <div class="wrap grid two">
      <div class="reveal">
        <p class="eyebrow" {A("house")}>{EN("house")}</p>
        <h2 class="display" style="margin-top:20px" {AH("ethos_h")}>{TR["ethos_h"]["en"]}</h2>
        <p class="lede" style="margin-top:28px" {A("ethos_lede")}>{EN("ethos_lede")}</p>
        <div class="ethos-stats">
          <div class="stat"><span class="num">6</span><span class="lbl" {A("stat_pieces")}>{EN("stat_pieces")}</span></div>
          <div class="stat"><span class="num">3</span><span class="lbl" {A("stat_finishes")}>{EN("stat_finishes")}</span></div>
          <div class="stat"><span class="num">1</span><span class="lbl" {A("stat_idea")}>{EN("stat_idea")}</span></div>
        </div>
        <a class="tlink" href="about.html" style="margin-top:40px"><span {A("read_philosophy")}>{EN("read_philosophy")}</span> {ARW}</a>
      </div>
      <div class="reveal d1">
        <div class="figure tall"><img src="images/organizer-fan.webp" alt="Organizer in brown, gray and black leather" loading="lazy" width="1100" height="880"></div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="eyebrow" {A("coll_label")}>{EN("coll_label")}</p>
        <h2 class="display" {A("coll_prev_h")}>{EN("coll_prev_h")}</h2>
        <p class="lede" {A("coll_prev_lede")}>{EN("coll_prev_lede")}</p>
      </div>
      <div class="prod-grid">{cards}</div>
      <div style="margin-top:48px" class="reveal"><a class="btn btn--ghost" href="collection.html"><span {A("view_all")}>{EN("view_all")}</span> {ARW}</a></div>
    </div>
  </section>

  <section class="section band">
    <div class="wrap grid two">
      <div class="reveal">
        <div class="figure" style="aspect-ratio:1/1"><img src="images/mascots.webp" alt="The Desk to Destinations leather characters" loading="lazy" width="1195" height="1195"></div>
      </div>
      <div class="reveal d1">
        <p class="eyebrow" {A("featured_theme")}>{EN("featured_theme")}</p>
        <h2 class="display" style="font-size:clamp(34px,5.6vw,72px);margin-top:20px" {AH("d2d_band_h")}>{TR["d2d_band_h"]["en"]}</h2>
        <p class="lede" style="margin-top:26px" {A("d2d_band_lede")}>{EN("d2d_band_lede")}</p>
        <a class="btn btn--solid" href="desk-to-destinations.html" style="margin-top:36px"><span {A("meet_family")}>{EN("meet_family")}</span> {ARW}</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap grid two">
      <div class="reveal">
        <div class="figure tall"><img src="images/briefcase.webp" alt="Executive with leather essentials and briefcase" loading="lazy" width="1100" height="1473"></div>
      </div>
      <div class="reveal d1">
        <p class="eyebrow" {A("materials")}>{EN("materials")}</p>
        <h2 class="display" style="font-size:clamp(30px,4.6vw,58px);margin-top:20px" {AH("materials_h")}>{TR["materials_h"]["en"]}</h2>
        <p class="lede" style="margin-top:26px" {A("materials_lede")}>{EN("materials_lede")}</p>
        <div class="pillars" style="margin-top:44px;grid-template-columns:1fr 1fr">
          <div class="pillar"><span class="k">01</span><h3 {A("mat1_h")}>{EN("mat1_h")}</h3><p {A("mat1_p")}>{EN("mat1_p")}</p></div>
          <div class="pillar"><span class="k">02</span><h3 {A("mat2_h")}>{EN("mat2_h")}</h3><p {A("mat2_p")}>{EN("mat2_p")}</p></div>
        </div>
      </div>
    </div>
  </section>
</main>
''' + footer()

# =====================================================================
# PAGE: COLLECTION
# =====================================================================
def page_collection():
    cards = "".join(product_card(p, ["","d1","d2","","d1","d2"][i]) for i, p in enumerate(PRODUCTS))
    filters = "".join(
        f'<button class="chip{" active" if k=="all" else ""}" data-filter="{k}" {A("filter_"+k)}>{EN("filter_"+k)}</button>'
        for k in ["all","desk","travel","everyday","gifting"])
    return head("Collection — Maison Valér",
                "The full Maison Valér collection: organizers, card holders, travel wallets, luggage tags and magnetic accessories in premium leather.",
                "collection") + header("collection") + f'''
<main>
  <section class="section section--tight" style="padding-top:clamp(120px,16vh,190px)">
    <div class="wrap">
      <div class="section-head reveal" style="max-width:900px">
        <p class="eyebrow" {A("coll_2026")}>{EN("coll_2026")}</p>
        <h1 class="display" style="font-size:clamp(44px,8vw,110px);margin-top:18px" {AH("coll_h")}>{TR["coll_h"]["en"]}</h1>
        <p class="lede" style="margin-top:28px" {A("coll_lede")}>{EN("coll_lede")}</p>
      </div>
      <div class="filterbar reveal" role="group" aria-label="Filter collection">{filters}</div>
      <div class="prod-grid">{cards}</div>
    </div>
  </section>
{feature_strip()}
</main>
''' + footer()

# =====================================================================
# PAGE: DESK TO DESTINATIONS
# =====================================================================
def page_d2d():
    archs = [
        dict(n="01", arch="strategist", img="life-organizer", sku="REXORA-11653",
             role="p1_sub", p="a1_p", use="a1_use", carry="a1_carry", cols=["brown","black","gray"]),
        dict(n="02", arch="minimalist", img="cardholder-gray", sku="MAGTEC-11659",
             role="a2_role" if "a2_role" in TR else "p2_sub", p="a2_p", use="a2_use", carry="a2_carry", cols=["brown","black","gray"]),
        dict(n="03", arch="explorer", img="life-passport", sku="LEPORT-11662",
             role="p3_sub", p="a3_p", use="a3_use", carry="a3_carry", cols=["brown","black","gray"]),
        dict(n="04", arch="identifier", img="luggage-tag", sku="LETHEG-11658",
             role="p4_sub", p="a4_p", use="a4_use", carry="a4_carry", cols=["brown","black","gray"]),
    ]
    blocks = ""
    for a in archs:
        sw = "".join(f'<span class="swatch sw-{c}" title="{EN("c_"+c)}"></span>' for c in a["cols"])
        blocks += f'''
      <article class="arch reveal">
        <div class="arch-media"><img src="images/{a['img']}.webp" alt="{EN("arch_"+a['arch'])}" loading="lazy" width="950" height="950"></div>
        <div>
          <span class="arch-index">{a['n']}</span>
          <h2 {AH("arch_"+a['arch'])}>{EN("arch_"+a['arch'])}</h2>
          <p class="role" {A(a['role'])}>{EN(a['role'])}</p>
          <p {A(a['p'])}>{EN(a['p'])}</p>
          <div class="arch-meta">
            <div><span class="k" {A("meta_bestfor")}>{EN("meta_bestfor")}</span><span class="v" {A(a['use'])}>{EN(a['use'])}</span></div>
            <div><span class="k" {A("meta_carries")}>{EN("meta_carries")}</span><span class="v" {A(a['carry'])}>{EN(a['carry'])}</span></div>
          </div>
          <div style="margin-top:30px;display:flex;gap:14px;align-items:center;flex-wrap:wrap">
            <div class="swatches" aria-hidden="true">{sw}</div>
            <span class="sku" style="font-size:11px;letter-spacing:.18em;color:var(--faint);text-transform:uppercase">{a['sku']}</span>
          </div>
        </div>
      </article>'''
    return head("Desk to Destinations — Maison Valér",
                "Desk to Destinations: a curated leather family — the Strategist, the Minimalist, the Explorer and the Identifier — built to move from desk to destination.",
                "d2d") + header("d2d") + f'''
<main>
  <section class="d2d-hero">
    <div class="hero-media" data-parallax="0.1"><img src="images/mascots.webp" alt="The Desk to Destinations leather characters at the airport" width="1195" height="1688" fetchpriority="high"></div>
    <div class="hero-inner wrap">
      <p class="hero-eyebrow eyebrow fade-seq d1" {A("featured_theme")}>{EN("featured_theme")}</p>
      <h1 class="hero-title display" style="font-size:clamp(46px,11vw,150px)" {AH("d2d_title")}>{TR["d2d_title"]["en"]}</h1>
      <p class="lede fade-seq d2" style="margin-top:30px;max-width:52ch" {A("d2d_lede")}>{EN("d2d_lede")}</p>
    </div>
  </section>

  <div class="ribbon" aria-hidden="true">
    <div class="ribbon-track">
      <span>The Strategist</span><span class="star">✦</span>
      <span>The Minimalist</span><span class="star">✦</span>
      <span>The Explorer</span><span class="star">✦</span>
      <span>The Identifier</span><span class="star">✦</span>
      <span>The Strategist</span><span class="star">✦</span>
      <span>The Minimalist</span><span class="star">✦</span>
      <span>The Explorer</span><span class="star">✦</span>
      <span>The Identifier</span><span class="star">✦</span>
    </div>
  </div>

  <section class="section section--tight">
    <div class="wrap" style="max-width:900px">
      <p class="eyebrow reveal" {A("the_idea")}>{EN("the_idea")}</p>
      <p class="manifesto reveal d1" style="max-width:26ch;margin-top:22px" {AH("idea_manifesto")}>{TR["idea_manifesto"]["en"]}</p>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">{blocks}</div>
  </section>
{feature_strip()}
</main>
''' + footer()

# =====================================================================
# PAGE: ABOUT
# =====================================================================
def page_about():
    return head("The House — Maison Valér",
                "At Maison Valér, design begins with restraint. Learn the philosophy behind the language of considered design.",
                "about") + header("about") + f'''
<main>
  <section class="section section--tight" style="padding-top:clamp(120px,16vh,190px)">
    <div class="wrap">
      <div class="section-head reveal" style="max-width:1000px">
        <p class="eyebrow" {A("house")}>{EN("house")}</p>
        <h1 class="display" style="font-size:clamp(44px,8vw,112px);margin-top:18px" {AH("about_h")}>{TR["about_h"]["en"]}</h1>
      </div>
      <div class="grid two">
        <div class="reveal"><div class="figure tall"><img src="images/life-organizer.webp" alt="Executive using a Maison Valér organizer" loading="lazy" width="950" height="1187"></div></div>
        <div class="reveal d1">
          <p class="manifesto" {AH("about_manifesto")}>{TR["about_manifesto"]["en"]}</p>
          <p class="lede" style="margin-top:30px" {A("about_p1")}>{EN("about_p1")}</p>
          <p class="lede" style="margin-top:20px" {A("about_p2")}>{EN("about_p2")}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section band">
    <div class="wrap">
      <div class="section-head reveal"><p class="eyebrow" {A("principles")}>{EN("principles")}</p><h2 class="display" style="margin-top:18px" {A("principles_h")}>{EN("principles_h")}</h2></div>
      <div class="pillars">
        <div class="pillar reveal"><span class="k">i.</span><h3 {A("pr1_h")}>{EN("pr1_h")}</h3><p {A("pr1_p")}>{EN("pr1_p")}</p></div>
        <div class="pillar reveal d1"><span class="k">ii.</span><h3 {A("pr2_h")}>{EN("pr2_h")}</h3><p {A("pr2_p")}>{EN("pr2_p")}</p></div>
        <div class="pillar reveal d2"><span class="k">iii.</span><h3 {A("pr3_h")}>{EN("pr3_h")}</h3><p {A("pr3_p")}>{EN("pr3_p")}</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap grid two">
      <div class="reveal d1">
        <p class="eyebrow" {A("fdd")}>{EN("fdd")}</p>
        <h2 class="display" style="font-size:clamp(30px,4.6vw,58px);margin-top:20px" {AH("fdd_h")}>{TR["fdd_h"]["en"]}</h2>
        <p class="lede" style="margin-top:26px" {A("fdd_lede")}>{EN("fdd_lede")}</p>
        <a class="tlink" href="desk-to-destinations.html" style="margin-top:36px"><span {A("explore_theme")}>{EN("explore_theme")}</span> {ARW}</a>
      </div>
      <div class="reveal"><div class="figure tall"><img src="images/airport-man.webp" alt="Traveller with Maison Valér essentials at the airport" loading="lazy" width="1500" height="1094"></div></div>
    </div>
  </section>
</main>
''' + footer()

# =====================================================================
# PAGE: CONTACT
# =====================================================================
def page_contact():
    opts = "".join(f'<option {A(p["key"]+"_name")}>{EN(p["key"]+"_name")}</option>' for p in PRODUCTS)
    return head("Contact — Maison Valér",
                "Enquire with Maison Valér for corporate gifting, wholesale and bespoke leather essentials.",
                "contact") + header("contact") + f'''
<main>
  <section class="section" style="padding-top:clamp(120px,16vh,190px)">
    <div class="wrap grid two" style="align-items:start;gap:clamp(40px,6vw,100px)">
      <div class="reveal">
        <p class="eyebrow" {A("enquire_label")}>{EN("enquire_label")}</p>
        <h1 class="display" style="font-size:clamp(40px,7vw,96px);margin-top:16px" {AH("contact_h")}>{TR["contact_h"]["en"]}</h1>
        <p class="lede" style="margin-top:26px" {A("contact_lede")}>{EN("contact_lede")}</p>
        <div class="contact-side" style="margin-top:52px">
          <div class="contact-item"><p class="k" {A("c_email")}>{EN("c_email")}</p><a class="v" href="mailto:hello@maisonvaler.com">hello@maisonvaler.com</a></div>
          <div class="contact-item"><p class="k" {A("c_studio")}>{EN("c_studio")}</p><p class="v" {A("c_studio_v")}>{EN("c_studio_v")}</p></div>
          <div class="contact-item"><p class="k" {A("c_trade")}>{EN("c_trade")}</p><p class="v" {A("c_trade_v")}>{EN("c_trade_v")}</p></div>
        </div>
      </div>

      <div class="reveal d1 form-card">
        <form class="form" novalidate>
          <div class="two-col">
            <div class="field"><label for="name" {A("f_name")}>{EN("f_name")}</label><input id="name" name="name" type="text" data-i18n-ph="ph_name" placeholder="{EN("ph_name")}" autocomplete="name"></div>
            <div class="field"><label for="email" {A("f_email")}>{EN("f_email")}</label><input id="email" name="email" type="email" placeholder="you@company.com" autocomplete="email"></div>
          </div>
          <div class="two-col">
            <div class="field"><label for="company" {A("f_company")}>{EN("f_company")}</label><input id="company" name="company" type="text" data-i18n-ph="ph_company" placeholder="{EN("ph_company")}" autocomplete="organization"></div>
            <div class="field"><label for="quantity" {A("f_quantity")}>{EN("f_quantity")}</label><input id="quantity" name="quantity" type="text" data-i18n-ph="ph_quantity" placeholder="{EN("ph_quantity")}"></div>
          </div>
          <div class="field">
            <label for="interest" {A("f_interest")}>{EN("f_interest")}</label>
            <select id="interest" name="interest">
              <option {A("opt_full")}>{EN("opt_full")}</option>
              {opts}
              <option {A("opt_d2d")}>{EN("opt_d2d")}</option>
              <option {A("opt_bespoke")}>{EN("opt_bespoke")}</option>
            </select>
          </div>
          <div class="field"><label for="message" {A("f_message")}>{EN("f_message")}</label><textarea id="message" name="message" data-i18n-ph="ph_message" placeholder="{EN("ph_message")}"></textarea></div>
          <div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap">
            <button class="btn btn--solid" type="submit"><span {A("btn_send")}>{EN("btn_send")}</span> {ARW}</button>
            <span class="form-status" role="status" aria-live="polite"></span>
          </div>
          <p class="form-note"><span {A("form_note")}>{EN("form_note")}</span> <a href="mailto:hello@maisonvaler.com" style="color:var(--cognac)">hello@maisonvaler.com</a></p>
        </form>
      </div>
    </div>
  </section>
</main>
''' + footer()

# =====================================================================
# Write
# =====================================================================
pages = {
    "index.html": page_home(),
    "collection.html": page_collection(),
    "desk-to-destinations.html": page_d2d(),
    "about.html": page_about(),
    "contact.html": page_contact(),
}
os.makedirs(OUT, exist_ok=True)
for fn, html in pages.items():
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fn, len(html), "chars")

with open(os.path.join(OUT, "js", "i18n.js"), "w", encoding="utf-8") as f:
    f.write("window.MV_LANGS=" + json.dumps(LANGS) + ";\n")
    f.write("window.MV_I18N=" + json.dumps(TR, ensure_ascii=False) + ";\n")
print("wrote js/i18n.js with", len(TR), "keys")

with open(os.path.join(OUT, "vercel.json"), "w") as f:
    f.write('{\n  "cleanUrls": true,\n  "trailingSlash": false\n}\n')
print("done")
