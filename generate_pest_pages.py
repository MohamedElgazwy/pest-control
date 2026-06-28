import os
import re

# Read index.html to extract common components
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# Extract header up to the closing </header>
header_match = re.search(r"^(.*?</header>)", index_html, re.DOTALL)
if header_match:
    header_html = header_match.group(1)
    # Fix active link highlights for subpages (make anchors point to index.html#about, etc.)
    header_html = header_html.replace('href="#about"', 'href="index.html#about"')
    header_html = header_html.replace('href="#services"', 'href="index.html#services"')
    header_html = header_html.replace('href="#work"', 'href="index.html#work"')
    header_html = header_html.replace('href="#testimonials"', 'href="index.html#testimonials"')
    header_html = header_html.replace('href="#faq"', 'href="index.html#faq"')
    header_html = header_html.replace('href="#contact"', 'href="index.html#contact"')
else:
    raise ValueError("Could not extract header from index.html")

# Extract floating contact bar
floating_bar_match = re.search(r"(<!-- --- FLOATING CONTACT BAR --- -->.*?<!-- --- END FLOATING CONTACT BAR --- -->)", index_html, re.DOTALL)
if floating_bar_match:
    floating_bar_html = floating_bar_match.group(1)
else:
    floating_bar_html = ""

# Extract footer from <footer> to </html>
footer_match = re.search(r"(<!-- --- 10. FOOTER --- -->.*)$", index_html, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    # Fix footer links
    footer_html = footer_html.replace('href="#about"', 'href="index.html#about"')
    footer_html = footer_html.replace('href="#services"', 'href="index.html#services"')
    footer_html = footer_html.replace('href="#work"', 'href="index.html#work"')
    footer_html = footer_html.replace('href="#faq"', 'href="index.html#faq"')
    footer_html = footer_html.replace('href="#contact"', 'href="index.html#contact"')
else:
    raise ValueError("Could not extract footer from index.html")

# Data for 10 pests
pests_data = {
    "pest-bedbugs": {
        "title_ar": "مكافحة بق الفراش وإبادة بيوضه نهائياً",
        "title_en": "Advanced Bed Bug Eradication Services",
        "meta_desc_ar": "الشركة الألمانية لمكافحة بق الفراش في مصر. نستخدم الحقن الميكروي والتعفير الحراري لإبادة البق وبويضاته بضمان معتمد 6 أشهر ومتابعة مجانية.",
        "meta_desc_en": "Professional bed bug control in Egypt. Utilizing micro-injections and thermal treatments for 100% egg and insect eradication. 6 months warranty.",
        "name_ar": "بق الفراش",
        "name_en": "Bed Bugs",
        "image": "assets/pest_bedbug.png",
        "intro_ar": "بق الفراش حشرة صغيرة طفيلية ليلية تتغذى على دماء الإنسان والحيوان. تنتشر بسرعة فائقة في غرف النوم والمفروشات وتبني مقاومة شرسة للمبيدات التقليدية، مما يتطلب تدخلاً علمياً لإبادتها بالكامل.",
        "intro_en": "Bed bugs are nocturnal parasitic insects feeding on blood. They hide inside mattress seams and wooden joints, developing high chemical resistance to standard insecticides, which demands premium thermal and chemical interventions.",
        "signs_ar": "بقع دم صغيرة داكنة على الملاءات والوسائد، فضلات سوداء متناهية الصغر في زوايا المرتبة، ووجود ندبات حمراء متتالية ومثيرة للحكة الشديدة على الجلد عند الاستيقاظ.",
        "signs_en": "Dark rusty spots on mattresses or sheets, microscopic black fecal specks in seam folds, and clusters of itchy red bite welts on your skin after sleeping.",
        "risks_ar": "يتسبب البق في الحساسية الجلدية الشديدة، والتهاب اللدغات، والأرق والتوتر العصبي نتيجة الحرمان من النوم الهادئ، ونادراً ما ينقل مسببات الأمراض ولكن تلوثه الميكروبي للمفروشات مرتفع للغاية.",
        "risks_en": "Severe skin allergies, secondary infections from scratch lesions, and chronic insomnia. They compromise the hygiene of soft textiles by spreading allergens.",
        "damage_ar": "تلف وتشويه المراتب الفاخرة والستائر والمفروشات بالأبواغ والفضلات الصعبة، مما يكبد الفنادق والمنشآت السكنية مبالغ طائلة لاستبدال الأثاث بالكامل.",
        "damage_en": "Irreversible staining on luxury mattresses, headboards, and heavy drapery, forcing commercial hospitality venues to discard valuable assets.",
        "process_desc_ar": "نستخدم تقنية التعفير الجاف للشقوق لخلخلة مخابئ البق، متبوعاً بحقن كيميائي ميكروي مباشر للبويضات، وتعقيم حراري بالبخار الجاف فائق السخونة لقتل أطوار الحشرة بالكامل.",
        "process_desc_en": "We apply deep-crevice dry dusting, followed by targeted chemical growth regulators for eggs, and finish with high-temperature dry steam treatments.",
        "prevention_ar": "اغسل أغطية الأسرة بانتظام عند درجة حرارة لا تقل عن 60 درجة مئوية، وافحص أمتعتك جيداً فور العودة من السفر، وسد أي شقوق في الحوائط المجاورة للأسرة.",
        "prevention_en": "Wash bedding at 60°C or higher, inspect luggage carefully after hotel stays, and seal any cracks in walls adjacent to bed frames.",
        "warranty_ar": "ضمان كامل لمدة 6 أشهر يشمل زيارتين مجانيتين للمتابعة والتدقيق للتأكد من خلو الموقع تماماً من يرقات الحشرة.",
        "warranty_en": "Comprehensive 6-month warranty backed by two scheduled follow-up inspections to audit and guarantee zero residual nymph activity.",
        "faq_q1_ar": "هل يجب مغادرة المنزل أثناء معالجة بق الفراش؟",
        "faq_a1_ar": "لا داعي للمغادرة بالكامل، نستخدم مواد آمنة تماماً وعديمة الرائحة ومصرحة بيئياً للاستخدام المنزلي الفاخر.",
        "faq_q1_en": "Do we need to vacate the house during treatment?",
        "faq_a1_en": "No. We utilize eco-neutral, odorless micro-capsules and targeted steam that require zero evacuation of residents.",
        "faq_q2_ar": "هل كم تستغرق عملية الإبادة؟",
        "faq_a2_ar": "تستغرق الجلسة من ساعتين إلى 4 ساعات حسب حجم الغرف المصابة ومستوى انتشار الحشرة.",
        "faq_q2_en": "How long does the eradication process take?",
        "faq_a2_en": "A standard professional session takes between 2 to 4 hours depending on the room size and severity of the infestation.",
        "related_1": "pest-cockroaches",
        "related_1_title": "الصراصير",
        "related_2": "pest-fleas",
        "related_2_title": "البراغيث"
    },
    "pest-cockroaches": {
        "title_ar": "إبادة الصراصير الألمانية والأمريكية بالجل الموضع",
        "title_en": "Professional Cockroach Control & Baiting",
        "meta_desc_ar": "تخلص من الصراصير نهائياً مع الشركة الألمانية. نستخدم الجل الجاذب والرش الوقائي للمطابخ والبالوعات دون رائحة وبضمان معتمد.",
        "meta_desc_en": "Get rid of German and American cockroaches permanently. We use targeted bait gels and chemical borders safe for food preparation zones.",
        "name_ar": "الصراصير",
        "name_en": "Cockroaches",
        "image": "assets/pest_cockroach.png",
        "intro_ar": "الصراصير (خاصة الألمانية والأمريكية) من أكثر الآفات خطورة ونقلاً للأمراض. تفضل العيش في الأماكن الرطبة كالمطابخ والحمامات، وتتكاثر بسرعة مذهلة وتنشر السموم الميكروبية على الأطعمة والأسطح.",
        "intro_en": "Cockroaches, particularly German and American varieties, are highly invasive vector pests. They thrive in dark, humid environments such as kitchens and drains, vectoring critical foodborne pathogens.",
        "signs_ar": "رؤية الحشرة نهاراً (دليل على تفاقم الإصابة)، وجود كبسولات البيض البنية الصغيرة، وبقع سوداء تشبه الفلفل الأسود في زوايا الدواليب.",
        "signs_en": "Sighting roaches during daylight (indicates high nest pressure), finding dark brown egg cases (oothecae), and black pepper-like droppings in cabinet hinges.",
        "risks_ar": "نقل بكتيريا السالمونيلا والإي كولاي، إفساد وتلويث الأغذية، وإفراز مواد مثيرة للحساسية والربو الشعبي، خصوصاً للأطفال وكبار السن.",
        "risks_en": "Transmission of Salmonella, E. coli, and gastroenteritis pathogens. Their shed skins and fecal materials trigger asthma and acute allergic respiratory reactions.",
        "damage_ar": "تلف وتلويث الأجهزة الكهربائية والمقابس (حيث تعشش بداخلها)، وتدمير السمعة التجارية للمطاعم والفنادق وإغلاقها قانونياً.",
        "damage_en": "Short-circuiting of kitchen appliances and electrical panels where they nest, and heavy regulatory fines or closure for food businesses.",
        "process_desc_ar": "تطبيق جل هرموني جاذب موضعياً في زوايا المطابخ والمصارف يقضي على المستعمرة بالكامل عن طريق التغذية الرجعية، ورش كيميائي عازل للمجاري والبالوعات.",
        "process_desc_en": "We place professional hormonal bait gels in deep hinges to poison the nest via secondary transfer, and deploy barrier sprays in drainage basins.",
        "prevention_ar": "تنظيف بقايا الأطعمة والدهون فوراً، إصلاح تسريبات المياه تحت الحوض، وإغلاق فتحات الصرف الصحي ليلاً بإحكام.",
        "prevention_en": "Clean food spills and grease immediately, repair plumbing leaks under sinks, and ensure sewer drains are sealed at night.",
        "warranty_ar": "ضمان كامل لمدة 12 شهراً للمنشآت السكنية يشمل المتابعة المجانية والرش الوقائي الفصلي.",
        "warranty_en": "Full 12-month warranty for residential properties, including quarterly preventive audits and boundary spray touch-ups.",
        "faq_q1_ar": "هل الجل المستخدم آمن على الأطفال والحيوانات الأليفة؟",
        "faq_a1_ar": "نعم، الجل يوضع في نقاط مخفية وعميقة جداً لا يمكن للأطفال الوصول إليها، وهو خالٍ من الأبخرة السامة تماماً.",
        "faq_q1_en": "Is the bait gel safe for children and household pets?",
        "faq_a1_en": "Yes. Gels are placed in deep, inaccessible structural crevices and contain zero airborne chemicals.",
        "faq_q2_ar": "هل نحتاج لتفريغ دواليب المطبخ؟",
        "faq_a2_ar": "في معظم الحالات لا حاجة لتفريغ الأواني، بفضل دقة تقنية الحقن الموضعي للمواد المعتمدة لدينا.",
        "faq_q2_en": "Do we need to empty the kitchen cabinets before you arrive?",
        "faq_a2_en": "No, cabinet evacuation is rarely required due to the localized nature of bait gel placement.",
        "related_1": "pest-ants",
        "related_1_title": "النمل",
        "related_2": "pest-flies",
        "related_2_title": "الذباب"
    },
    "pest-termites": {
        "title_ar": "مكافحة النمل الأبيض وحقن التربة قبل وبعد البناء",
        "title_en": "Subterranean Termite Barrier Services",
        "meta_desc_ar": "الشركة الألمانية رائدة مكافحة النمل الأبيض في مصر بضمان 10 سنوات. نقوم بإنشاء خنادق كيميائية عازلة وحقن الأساسات والباركيه.",
        "meta_desc_en": "Subterranean termite control in Egypt. We establish liquid chemical barriers and sub-slab soil barriers with a 10-year official warranty.",
        "name_ar": "النمل الأبيض",
        "name_en": "Termites",
        "image": "assets/النمل الابيض.jpg",
        "intro_ar": "النمل الأبيض (الأرضة) من أخطر الآفات المدمرة للممتلكات. يتغذى على مادة السيليلوز الموجودة في الأخشاب والخرسانة، ويعيش في مستعمرات تحت الأرض تضم الملايين، مما يجعله خطراً صامتاً يهدد سلامة المبنى الإنشائية.",
        "intro_en": "Subterranean termites are structurally catastrophic pests. Feeding non-stop on cellulose in wood, cardboard, and drywall, their massive colonies burrow underneath concrete foundations, leading to quiet structure failures.",
        "signs_ar": "ظهور أنابيب طينية على الجدران، سماع صوت أجوف عند النقر على الباركيه أو حلوق الأبواب، وتساقط نثارة تشبه الرمل الناعم أسفل الخشب.",
        "signs_en": "Earthen mud tubes crawling up walls, a hollow sound when tapping timber, and fine wood dust accumulate near baseboards.",
        "risks_ar": "رغم أنه لا يسبب خطراً صحياً مباشراً للبشر، إلا أن مستعمراته تتسبب في انهيارات مفاجئة للجدران والأسقف الخشبية وتدمير كامل للأثاث والكتب.",
        "risks_en": "While they do not bite humans, their tunneling poses extreme collapse hazards to wooden structures, roofs, floors, and archives.",
        "damage_ar": "تآكل وتدمير أساسات البناء، تلف الباركيه الفاخر، حلوق الأبواب الخشبية، والمطابخ، مما يستدعي ترميمات هندسية باهظة التكلفة.",
        "damage_en": "Severe foundation erosion, ruined hardwood floors, door frames, and built-in wardrobes, causing costly engineering repairs.",
        "process_desc_ar": "حقن التربة والأساسات بمبيدات طويلة الأمد لإنشاء حاجز كيميائي عازل يمنع تسلل النمل من باطن الأرض، ومعالجة الأخشاب المصابة بالحقن المباشر.",
        "process_desc_en": "We perform sub-slab drilling and high-pressure chemical soil injections to build an impermeable liquid barrier, combined with timber treatment.",
        "prevention_ar": "تجنب تخزين الأخشاب أو الكرتون بجانب أساسات الفيلا، التخلص من رطوبة الجدران فوراً، وفحص حديقة المنزل دورياً.",
        "prevention_en": "Avoid storing firewood or timber against the house foundation, address subterranean plumbing dampness immediately, and clear dead roots.",
        "warranty_ar": "ضمان هندسي معتمد لمدة 10 سنوات يشمل الفحص السنوي الوقائي المجاني للموقع.",
        "warranty_en": "10-year official certificate warranty including annual preventive inspection audits and soil barrier integrity checks.",
        "faq_q1_ar": "كيف يتم حقن المبيد تحت الباركيه دون إتلافه؟",
        "faq_a1_ar": "نستخدم إبر حقن متناهية الصغر من خلال فواصل الباركيه أو أسفل النعلات الخشبية، مما يضمن معالجة تامة دون أي تشويه للأرضيات الفاخرة.",
        "faq_q1_en": "How do you inject pesticide under hardwood floors without damage?",
        "faq_a1_en": "We use specialized ultra-fine injection needles through structural gaps or beneath baseboards, ensuring zero visual damage.",
        "faq_q2_ar": "هل يفضل مكافحة النمل الأبيض قبل صبة النظافة؟",
        "faq_a2_ar": "بكل تأكيد، الرش المباشر للتربة قبل البناء هو خط الدفاع الأقوى والأوفر لإنشاء عازل كامل لمدى الحياة.",
        "faq_q2_en": "Is it better to spray the soil before pouring the concrete slab?",
        "faq_a2_en": "Yes, pre-construction chemical soil saturation is the most effective and cost-efficient defense for permanent prevention.",
        "related_1": "pest-woodborers",
        "related_1_title": "سوس الخشب",
        "related_2": "pest-ants",
        "related_2_title": "النمل"
    },
    "pest-woodborers": {
        "title_ar": "علاج سوس الخشب والديدان الناخرة بالحقن الكيميائي",
        "title_en": "Wood Borer & Beetle Treatment",
        "meta_desc_ar": "عالج سوس الخشب فوراً مع الشركة الألمانية. نستخدم تقنية حقن الشقوق الكيميائية والتعفير لضمان حماية الأسقف والأثاث الأثري والأبواب.",
        "meta_desc_en": "Eradicate wood-boring beetles and timber worms. Micro-injection of deep wood channels and gas fumigation under strict safety measures.",
        "name_ar": "سوس الخشب",
        "name_en": "Wood Borers",
        "image": "assets/سوس الخشب.png",
        "intro_ar": "سوس الخشب هو يرقات خنافس الخشب التي تنخر في الهياكل الخشبية الصلبة لسنوات طويلة. تتغذى اليرقات على الألياف الداخلية صانعةً أنفاقاً مدمرة، وتتحول لخنافس بالغة تخرج تاركةً ثقوباً تشوه المظهر الخارجي وتضعف الخشب.",
        "intro_en": "Wood borers are the larval stages of wood-destroying beetles. They spend years burrowing deep tunnels inside structural beams and luxury furniture, emerging as adults and leaving structural integrity severely weakened.",
        "signs_ar": "ظهور ثقوب دائرية صغيرة جداً على سطح الخشب، تساقط مستمر لنشارة الخشب الناعمة كالبودرة، وسماع صوت خافت جداً للنخر في سكون الليل.",
        "signs_en": "Fresh tiny exit holes in wood surfaces, continuous accumulation of powdery wood dust (frass), and faint clicking sounds inside timber.",
        "risks_ar": "يتسبب سوس الخشب في تهديد سلامة الأسقف والتعريشات الخشبية، ويدمر الأثاث التاريخي والأثري الثمين، ويؤدي إلى انهيار القطع المصابة عند تحميل الأوزان عليها.",
        "risks_en": "Structural failures of wooden rafters and structural pillars, total loss of valuable heritage furniture, and decay of load-bearing wood.",
        "damage_ar": "تدمير البنية الداخلية للأبواب الفاخرة، المطابخ، الأسقف الخشبية، والتحف الفنية، مما يقلل قيمتها المادية تماماً.",
        "damage_en": "Destruction of custom kitchen cabinets, ceiling beams, and artistic wooden sculptures, resulting in total loss of asset value.",
        "process_desc_ar": "تنظيف الشقوق وحقن قنوات النخر بمحاليل كيميائية نفاذة عالية التركيز تقتل اليرقات في مكانها، مع دهان الأسطح بطبقة وقائية تمنع عودة الخنافس لوضع البيض.",
        "process_desc_en": "We clean and inject deep boring channels with high-concentration timber preservatives, and coat the exterior with a sealing repellant.",
        "prevention_ar": "عزل الخشب بدهانات واقية ضد الرطوبة، عدم إدخال أثاث مصاب للمنزل، وفحص الأخشاب المعرضة للرطوبة باستمرار.",
        "prevention_en": "Apply specialized varnishes to repel beetles, inspect incoming timber products, and minimize indoor moisture exposure.",
        "warranty_ar": "ضمان كامل لمدة سنتين يشمل زيارات فحص نصف سنوية لمعالجة أي نشاط متجدد ليرقات سوس الخشب.",
        "warranty_en": "2-year comprehensive service warranty including bi-annual inspection check-ups to intercept any late-emerging larvae.",
        "faq_q1_ar": "هل تضمن المعالجة عدم عودة السوس للأبد؟",
        "faq_a1_ar": "نعم، المواد المستخدمة تتغلغل عميقاً في مسام الخشب وتبقى نشطة لعدة سنوات، مما يمنع تكاثر أي يرقات جديدة بشكل دائم.",
        "faq_q1_en": "Does the treatment guarantee termites/borers never return?",
        "faq_a1_en": "Yes, our active chemical agents bind with the wood fibers and remain toxic to wood-boring larvae for several years.",
        "faq_q2_ar": "هل تتأثر دهانات الأثاث بالمعالجة؟",
        "faq_a2_ar": "لا داعي للقلق، نستخدم محاليل حقن متخصصة للغاية لا تترك بقعاً ولا تتسبب في إتلاف الألوان أو الدهانات الخارجية للقطع الفاخرة.",
        "faq_q2_en": "Will the treatment damage the varnish or paint on my furniture?",
        "faq_a2_en": "No. Our premium chemical carriers are transparent, quick-drying, and leave no residue or discoloration on luxury finishes.",
        "related_1": "pest-termites",
        "related_1_title": "النمل الأبيض",
        "related_2": "pest-spiders",
        "related_2_title": "العناكب"
    },
    "pest-ants": {
        "title_ar": "مكافحة النمل الأسود والنمل الناري بالطعوم الهرمونية",
        "title_en": "Residential & Commercial Ant Control",
        "meta_desc_ar": "تخلص من مستعمرات النمل في منزلك وحديقتك. نستخدم محطات طعوم ذكية تقضي على الملكة نهائياً بضمان معتمد وزيارات متابعة دورية.",
        "meta_desc_en": "Eradicate house ants and fire ants. Safe micro-granules and biological baiting stations that eliminate the entire nest starting from the queen.",
        "name_ar": "النمل",
        "name_en": "Ants",
        "image": "assets/مكافحة النمل.png",
        "intro_ar": "النمل من أكثر الآفات شيوعاً وإزعاجاً في البيئات السكنية والتجارية. يتحرك في مسارات منظمة للبحث عن الغذاء، وينشئ أعشاشاً ضخمة تحت البلاط أو في فراغات الجدران، مما يسبب إزعاجاً مستمراً وتشويهاً للمظهر العام.",
        "intro_en": "Ants are common household pests that travel in structured foraging columns. Nester ants burrow underneath tiles and wall voids, causing continuous aesthetic disruptions and food hygiene failures.",
        "signs_ar": "رؤية طوابير النمل على الجدران والأسطح، وجود كومة من التراب الناعم بجوار فواصل السيراميك، وتجمع النمل على السكريات والأطعمة المكشوفة.",
        "signs_en": "Active marching columns along walls or counters, piles of excavated fine sand next to tile grout joints, and swarms around food.",
        "risks_ar": "يتسبب النمل الناري في لدغات مؤلمة تسبب حساسية جلدية وتورماً، كما يلوث النمل العادي الأطعمة والحلويات بالميكروبات التي يحملها من الأرض.",
        "risks_en": "Fire ant stings cause painful, burning pustules that trigger skin allergies. Common ants contaminate pantry items and workspace dining tables.",
        "damage_ar": "تفريغ التراب من أسفل السيراميك والبلاط يؤدي إلى هبوط الأرضيات تدريجياً، كما يعشش النمل في الأجهزة الإلكترونية مسبباً أعطالاً.",
        "damage_en": "Erosion of sand layers beneath floor tiles leads to hollow spots and sinking grout, alongside nesting inside home routers and appliances.",
        "process_desc_ar": "نشر محطات طعوم هرمونية متطورة يفضلها النمل على السكر، فيقوم بنقلها إلى المستعمرة وتغذية الملكة عليها، مما يؤدي لموت العش بأكمله.",
        "process_desc_en": "We deploy slow-acting bait stations containing targeted hormones. Workers carry the bait back, eradicating the queen and the entire nest.",
        "prevention_ar": "حفظ السكريات والأطعمة في علب محكمة الإغلاق، مسح الأسطح بالماء والخل لقطع مسارات النمل، وسد الفجوات بين السيراميك.",
        "prevention_en": "Store sugary foods in airtight containers, wipe counters with mild vinegar to disrupt pheromone trails, and keep floor grout sealed.",
        "warranty_ar": "ضمان معتمد لمدة 6 أشهر للمنازل يشمل إعادة المعالجة الفورية مجاناً في حال ظهور أي مسارات جديدة للنمل.",
        "warranty_en": "6-month solid warranty including free immediate retreatment if any new ant trails emerge within the coverage window.",
        "faq_q1_ar": "لماذا لا ينصح برش النمل بالمبيدات العادية؟",
        "faq_a1_ar": "المبيدات التقليدية تقتل النمل الظاهر فقط وتدفع باقي المستعمرة للانقسام والانتشار في أكن أخرى، بينما الطعوم تقضي على أصل المشكلة (الملكة).",
        "faq_q1_en": "Why shouldn't we use standard aerosol sprays for ants?",
        "faq_a1_en": "Standard sprays only kill foraging workers, triggering stress budding where the nest splits into multiple new colonies. Baits target the queen.",
        "faq_q2_ar": "كم من الوقت تستغرق الطعوم للقضاء على النمل؟",
        "faq_a2_ar": "تظهر النتائج الإيجابية خلال 3 إلى 7 أيام، حيث يبدأ النمل في الاختفاء تدريجياً حتى يتلاشى تماماً بعد تدمير الملكة.",
        "faq_q2_en": "How long does it take for the bait to destroy the nest?",
        "faq_a2_en": "You will notice a sharp reduction in ant traffic within 3 to 7 days, leading to complete nest collapse once the queen is eliminated.",
        "related_1": "pest-cockroaches",
        "related_1_title": "الصراصير",
        "related_2": "pest-rodents",
        "related_2_title": "القوارض"
    },
    "pest-mosquitoes": {
        "title_ar": "مكافحة البعوض وضباب الحدائق والرش البيولوجي",
        "title_en": "Outdoor Mosquito Fogging & Larvicide",
        "meta_desc_ar": "الشركة الألمانية لمكافحة البعوض والناموس في مصر. نستخدم أجهزة الضباب الحراري والرش البيولوجي ليرقات المياه الراكدة بضمان معتمد.",
        "meta_desc_en": "Professional mosquito control and yard fogging. Targeted larvicide treatments for standing water and thermal outdoor foggers in Egypt.",
        "name_ar": "البعوض",
        "name_en": "Mosquitoes",
        "image": "assets/ابادة البعوض.jpg",
        "intro_ar": "البعوض (الناموس) هو الناقل الأول للأوبئة والفيروسات في العالم. ينشط في الحدائق والمناطق الرطبة حول برك المياه، وتسبب لدغات إناث البعوض حكة شديدة وإزعاجاً يعكر صفو الأماكن المفتوحة ويهدد الصحة العامة.",
        "intro_en": "Mosquitoes are globally hazardous disease vectors. Breeding in stagnant water and swimming pool fringes, they populate garden areas, rendering outdoor lounging impossible and carrying clinical vector risks.",
        "signs_ar": "سماع طنين الحشرة المزعج ليلاً، ظهور لدغات حمراء متورمة ومثيرة للحكة على الجلد، ورؤية يرقات سابحة في المسابح وبرك المياه الراكدة.",
        "signs_en": "High-pitched whining near ears at night, itchy red skin welts, and active wriggling mosquito larvae in unchlorinated water basins.",
        "risks_ar": "نقل فيروسات خطيرة مثل حمى الضنك، الملاريا، وفيروس غرب النيل، بالإضافة إلى التسبب في حساسية جلدية حادة والتهاب الجروح الناجمة عن اللدغ.",
        "risks_en": "Transmission of dangerous pathogens like Dengue Fever and Malaria, along with secondary bacterial skin infections from scratch lesions.",
        "damage_ar": "تأثير سلبي كبير على الفنادق والمنتجعات السياحية والمطاعم المفتوحة حيث ينفر الزوار بسبب انتشار الناموس الكثيف.",
        "damage_en": "Severe financial impact on outdoor restaurants and luxury resorts by driving guests away due to mosquito discomfort.",
        "process_desc_ar": "تطبيق الرش البيولوجي لقتل اليرقات في برك المياه، متبوعاً بالتعفير وضباب الحدائق الحراري (Fogger) للقضاء على البعوض البالغ المستقر في الأشجار.",
        "process_desc_en": "We apply biological larvicide to standing water, followed by thermal fogging of trees and foliage to target adult resting populations.",
        "prevention_ar": "تفريغ حاويات المياه المكشوفة بانتظام، تغيير مياه المزهريات وأوعية الحيوانات يومياً، والرش الوقائي للحديقة قبل غروب الشمس.",
        "prevention_en": "Empty open water containers weekly, replace pet bowl water daily, and schedule regular preventive yard sprays before sunset.",
        "warranty_ar": "نقدم برامج تعاقدية دورية (شهرية أو نصف شهرية) لضمان حماية مستمرة للحدائق والمساحات المفتوحة طوال موسم الصيف.",
        "warranty_en": "Flexible seasonal contracts (monthly or bi-weekly visits) designed to maintain a mosquito-free yard during summer peak months.",
        "faq_q1_ar": "هل المواد المستخدمة في مكافحة الناموس تضر بالنباتات أو الحيوانات الأليفة؟",
        "faq_a1_ar": "لا، نستخدم مبيدات وقائية متخصصة ومعتمدة بيئياً لا تؤثر على صحة الأشجار، الزهور، أو الحيوانات الأليفة في الحديقة.",
        "faq_q1_en": "Does the mosquito fogging harm garden plants or pets?",
        "faq_a1_en": "No, our specialized green pyrethroids are eco-friendly, non-phytotoxic, and safe for domestic dogs and cats once dry.",
        "faq_q2_ar": "ما هو أفضل وقت لإجراء مكافحة الناموس؟",
        "faq_a2_ar": "يفضل الرش في الصباح الباكر أو قبل الغروب مباشرة، حيث تكون الحشرات البالغة في أقصى درجات نشاطها واستقرارها على أوراق الشجر.",
        "faq_q2_en": "What is the best time of day to perform mosquito fogging?",
        "faq_a2_en": "Early morning or late afternoon (dusk) is ideal, when adult mosquitoes are most active and resting on foliage.",
        "related_1": "pest-flies",
        "related_1_title": "الذباب",
        "related_2": "pest-fleas",
        "related_2_title": "البراغيث"
    },
    "pest-flies": {
        "title_ar": "مكافحة الذباب بالمنشآت الغذائية والمصائد الضوئية",
        "title_en": "Commercial Fly Control & Interceptors",
        "meta_desc_ar": "الشركة الألمانية تقدم حلول مكافحة الذباب للمطاعم والمنشآت الغذائية بمصر. نركب مصائد ضوئية لاصقة ونستخدم طعوماً جاذبة آمنة.",
        "meta_desc_en": "Fly control for restaurants and food production. UV glue-trap installation, pheromone baits, and sanitation audits in Egypt.",
        "name_ar": "الذباب",
        "name_en": "Flies",
        "image": "assets/مكافحة الذباب.jpg",
        "intro_ar": "الذباب من أكثر الآفات المزعجة والناقلة للأمراض في بيئات تحضير الأطعمة. يتنقل الذباب بين النفايات والأغذية المكشوفة، مما يجعله خطراً داهماً يهدد سلامة الغذاء ويثير اشمئزاز العملاء في المطاعم والمنشآت الفاخرة.",
        "intro_en": "Flies are high-risk sanitary pests in food service operations. Flying between garbage and clean meals, they transfer dangerous pathogens, compromising food safety and ruining the dining experience.",
        "signs_ar": "رؤية الحشرات البالغة تطير حول الأطعمة، تراكم بقع الفضلات الداكنة على الجدران والأسقف، وظهور اليرقات (الدود الأبيض) في النفايات.",
        "signs_en": "Active flies buzzing around food prep stations, dark fecal spots on ceiling panels, and crawling maggots inside garbage bins.",
        "risks_ar": "نقل التيفود، الكوليرا، والدوسنتاريا، بالإضافة إلى نقل بكتيريا التسمم الغذائي وتلويث الأسطح باللعاب والفضلات بشكل مستمر.",
        "risks_en": "Transmission of Typhoid, Cholera, and Dysentery. They harbor over 100 pathogens on their legs, triggering food poisoning cases.",
        "damage_ar": "إفساد المواد الغذائية الخام، إغلاق المطاعم قانونياً نتيجة فشل تفتيش الصحة، وتشويه سمعة العلامات التجارية للمطاعم الفاخرة.",
        "damage_en": "Ruined food inventory, regulatory shut-downs for food businesses, and severe damage to restaurant online ratings.",
        "process_desc_ar": "تركيب مصائد ضوئية لاصقة صامتة (لا تصدر صوتاً ولا تفتت الحشرات)، وتطبيق طعوم فرمونية جاذبة متخصصة حول مناطق القمامة والمداخل.",
        "process_desc_en": "We install silent UV glue-board traps (no zapping/splattering) and deploy pheromone-based fly baits around garbage holding zones.",
        "prevention_ar": "تغطية صناديق النفايات بإحكام، تركيب ستائر هوائية على المداخل الرئيسية، وتنظيف مصارف الأرضيات في المطابخ بانتظام.",
        "prevention_en": "Ensure garbage lids are kept closed, maintain active air curtains at entrances, and clean floor drains weekly.",
        "warranty_ar": "برامج وقائية شهرية تشمل فحص المصائد وصيانتها واستبدال ألواح الغراء اللاصقة لضمان تحكم دائم.",
        "warranty_en": "Monthly preventive maintenance service covering trap inspections, glue-board replacements, and boundary bait updates.",
        "faq_q1_ar": "لماذا نفضل المصائد اللاصقة على الصاعق الكهربائي المعتاد؟",
        "faq_a1_ar": "الصاعق الكهربائي يتسبب في تفتيت جزيئات الحشرة وتطاير بكتيريا ملوثة للأغذية في الهواء، بينما المصيدة اللاصقة تحتجز الذبابة بالكامل بصمت وأمان.",
        "faq_q1_en": "Why are UV glue traps preferred over electric grid zappers?",
        "faq_a1_en": "Electric zappers vaporize fly body parts, releasing airborne bacteria into food-prep zones. Glue traps capture them whole and silently.",
        "faq_q2_ar": "هل الطعوم المستخدمة حول المداخل سامة؟",
        "faq_a2_ar": "الطعوم توضع بعيداً عن أسطح تحضير الغذاء، وتتميز بجاذبية فائقة للذباب مع مستويات أمان ممتازة وصديقة للبيئة.",
        "faq_q2_en": "Are the baits used around entrance doors toxic?",
        "faq_a2_en": "No. Baits are applied to non-food contact areas and attract flies away from clean dining spaces using organic food scents.",
        "related_1": "pest-mosquitoes",
        "related_1_title": "البعوض",
        "related_2": "pest-cockroaches",
        "related_2_title": "الصراصير"
    },
    "pest-fleas": {
        "title_ar": "إبادة البراغيث والقراد في السجاد والحدائق",
        "title_en": "Flea & Tick Eradication Programs",
        "meta_desc_ar": "الشركة الألمانية لمكافحة البراغيث والقراد في مصر. نستخدم مبيدات آمنة للحيوانات الأليفة مع تعقيم المفروشات لضمان القضاء التام.",
        "meta_desc_en": "Get rid of fleas and ticks in your home and lawn. Safe chemical treatments targeting larvae and adults. Safe for pets and families.",
        "name_ar": "البراغيث",
        "name_en": "Fleas",
        "image": "assets/ابادة البراغيث.png",
        "intro_ar": "البراغيث حشرات طفيلية صغيرة قفازة تتغذى على دماء الثدييات (خاصة القطط والكلاب). تنتقل البراغيث بسرعة للمفروشات والسجاد، وتسبب لدغات متكررة ومؤلمة للإنسان والحيوان، مما يجعل السيطرة عليها أمراً ملحاً لسلامة المنزل.",
        "intro_en": "Fleas are small, wingless, jumping parasites feeding on mammalian blood. Easily introduced by domestic cats and dogs, they spread rapidly through carpets, causing painful bites and veterinary discomfort.",
        "signs_ar": "رؤية حشرات سوداء صغيرة تقفز في السجاد، حكة مستمرة وشديدة للحيوانات الأليفة، ولدغات حمراء صغيرة حول الكاحلين والساقين.",
        "signs_en": "Tiny black insects jumping off rug fibers, excessive scratching by your pets, and clusters of tiny red bites around your ankles.",
        "risks_ar": "نقل ديدان الأمعاء للكلاب والقطط، التسبب في فقر الدم (الأنيميا) للحيوانات الصغيرة، ونقل أمراض بكتيرية مثل التيفوس والتسبب في حساسية اللدغ.",
        "risks_en": "Transmission of tapeworms to pets, causing severe anemia in small puppies or kittens, and vectoring murine typhus bacteria to humans.",
        "damage_ar": "تلوث السجاد والمفروشات بالبويضات واليرقات، وصعوبة استخدام الحدائق المنزلية نتيجة انتشار البراغيث في الأعشاب.",
        "damage_en": "Widespread contamination of rugs and upholstery with microscopic eggs, and unusable lawns due to lawn flea infestations.",
        "process_desc_ar": "رش السجاد والستائر بمواد وقائية تمنع نمو يرقات البراغيث (IGRs)، متبوعاً بمعالجة رطبة للحدائق والمساحات العشبية التي تتردد عليها الحيوانات.",
        "process_desc_en": "We mist carpets with insect growth regulators (IGRs) that prevent larval shedding, and perform wet chemical rinsing on garden lawns.",
        "prevention_ar": "تنظيف السجاد بالمكنسة الكهربائية يومياً، غسل فراش الحيوانات الأليفة بالماء الساخن، وعلاج الحيوانات لدى الطبيب البيطري بانتظام.",
        "prevention_en": "Vacuum carpets daily to remove eggs, wash pet beds weekly at high temperatures, and apply vet-approved flea treatments on pets.",
        "warranty_ar": "ضمان كامل لمدة 6 أشهر للمنازل يشمل إعادة الرش مجاناً في حال رصد أي نشاط للبراغيث خلال فترة الضمان.",
        "warranty_en": "6-month solid warranty covering free immediate retreatment if any flea activity is detected within the coverage period.",
        "faq_q1_ar": "هل يجب معالجة الحيوانات الأليفة بالتزامن مع رش المنزل؟",
        "faq_a1_ar": "نعم، بكل تأكيد. يجب تطبيق علاج البراغيث البيطري على الحيوان بالتزامن مع معالجتنا للمنزل لضمان عدم تكرار العدوى.",
        "faq_q1_en": "Should pets be treated at the same time the house is sprayed?",
        "faq_a1_en": "Absolutely. You must apply vet-approved flea drops (spot-on) to your pets while we treat the floors to break the life cycle.",
        "faq_q2_ar": "هل تموت يرقات البراغيث بالرش العادي؟",
        "faq_a2_ar": "يرقات البراغيث تعيش في عمق أنسجة السجاد وتحميها شرانق قوية، لذلك نستخدم منظمات نمو متخصصة تخترق الشرانق وتقضي عليها.",
        "faq_q2_en": "Does standard chemical spraying kill flea larvae?",
        "faq_a2_en": "Larvae weave protective silk cocoons that resist standard contact sprays. We combine standard formulas with special ovicides (IGRs).",
        "related_1": "pest-bedbugs",
        "related_1_title": "بق الفراش",
        "related_2": "pest-ants",
        "related_2_title": "النمل"
    },
    "pest-rodents": {
        "title_ar": "مكافحة الفئران والقوارض بمحطات طعوم مغلقة",
        "title_en": "Exclusion-First Rodent & Rat Control",
        "meta_desc_ar": "إبادة الفئران والجرذان نهائياً مع الشركة الألمانية. نستخدم محطات طعوم آمنة وسد مسارات الدخول بضمان معتمد وزيارات متابعة دورية.",
        "meta_desc_en": "Commercial and residential rat control in Egypt. Tamper-resistant bait stations, physical entry exclusion, and tracking sensors.",
        "name_ar": "القوارض",
        "name_en": "Rodents",
        "image": "https://images.unsplash.com/photo-1425082661705-1834bfd09dca?auto=format&fit=crop&q=80&w=800",
        "intro_ar": "الفئران والجرذان من أكثر الآفات ذكاءً وتدميراً للمنشآت. تبحث عن الدفء والغذاء في المخازن والبيوت، وتمتلك قدرة هائلة على قضم المواد الصلبة، بالإضافة إلى نقلها لأمراض قاتلة، مما يتطلب استراتيجية مكافحة متكاملة تعتمد على سد المنافذ.",
        "intro_en": "Rats and mice are highly intelligent and destructive structural pests. Burrowing into pantries and wall cavities for warmth, they gnaw through building materials and carry severe vector-borne clinical risks.",
        "signs_ar": "سماع أصوات خربشة في الأسقف أو الجدران ليلاً، وجود فضلات سوداء متطاولة، ورؤية علامات قضم على الأسلاك الكهربائية أو الأبواب الخشبية.",
        "signs_en": "Scratching noises in ceilings or drywalls at night, dark spindle-shaped droppings, and fresh gnaw marks on baseboards or wiring.",
        "risks_ar": "نقل مرض الطاعون، فيروس هانتا، والتهاب السحايا، بالإضافة إلى تلويث الأطعمة بالبول والفضلات ونقل البكتيريا المعوية.",
        "risks_en": "Transmission of Leptospirosis, Hantavirus, and Salmonella. Their urine contains proteins that trigger severe respiratory allergies.",
        "damage_ar": "قضم الأسلاك الكهربائية يتسبب في حدوث ماس كهربائي وحرائق ضخمة، كما تدمر الفئران الكرتون والتغليف في المخازن التجارية.",
        "damage_en": "Gnawing on active electrical wiring causing short-circuits and structural fires, alongside ruining paper goods and raw stock.",
        "process_desc_ar": "بدء عملية فحص دقيقة لتحديد منافذ الدخول وسدها بألياف فولاذية عازلة، تليها زراعة محطات طعوم مغلقة وآمنة تحتوي على سموم مسيلة للدم.",
        "process_desc_en": "We locate and seal all entries with steel mesh (exclusion), then place secure, child-proof bait stations with professional rodenticides.",
        "prevention_ar": "تقليم أغصان الأشجار القريبة من النوافذ، سد الفتحات أسفل الأبواب بمصدات مطاطية صلبة، وعدم ترك طعام الحيوانات مكشوفاً في الخارج.",
        "prevention_en": "Trim overhanging tree branches away from windows, install heavy-duty sweeps under doors, and avoid leaving pet kibble outside.",
        "warranty_ar": "ضمان كامل لمدة سنة للمنشآت السكنية والتجارية يشمل متابعة شهرية وصيانة لمحطات الطعوم وسد أي منافذ جديدة.",
        "warranty_en": "1-year solid warranty for commercial and residential zones, including monthly inspections and maintenance of bait systems.",
        "faq_q1_ar": "هل الفئران تموت داخل المنزل وتسبب روائح كريهة؟",
        "faq_a1_ar": "لا، نستخدم طعوماً حديثة تسبب جفافاً تدريجياً للفأر وتدفعه للبحث عن الهواء والمياه في الخارج، مما يجعله يموت خارج المنزل دون ترك أي رائحة.",
        "faq_q1_en": "Will poisoned rats die inside the ceiling and smell?",
        "faq_a1_en": "No. Our premium anticoagulants dry the rodent from the inside and trigger a drive to find water outdoors, preventing indoor rot smell.",
        "faq_q2_ar": "هل محطات الطعوم آمنة للأطفال والكلاب؟",
        "faq_a2_ar": "نعم، الطعوم توضع داخل صناديق بلاستيكية قوية ومقفلة بمفاتيح خاصة (Tamper-proof)، ومصممة بفتحة صغيرة لدخول الفأر فقط.",
        "faq_q2_en": "Are the bait stations safe for toddlers and pets?",
        "faq_a2_en": "Yes. We use heavy-duty, locked, tamper-resistant poly-boxes that cannot be opened by dogs or kids, sized only for rodent entry.",
        "related_1": "pest-ants",
        "related_1_title": "النمل",
        "related_2": "pest-cockroaches",
        "related_2_title": "الصراصير"
    },
    "pest-spiders": {
        "title_ar": "مكافحة العناكب ورش الحواجز الوقائية طويلة الأمد",
        "title_en": "Residential & Commercial Spider Control",
        "meta_desc_ar": "الشركة الألمانية لمكافحة العناكب وإزالة النسيج في مصر. نستخدم رشاً عازلاً للمرتفعات والشقوق الخارجية لمنع العناكب نهائياً.",
        "meta_desc_en": "Eradicate spiders and clear webs from ceilings. Long-lasting repellent border sprays on eaves and window frames. Certified safety.",
        "name_ar": "العناكب",
        "name_en": "Spiders",
        "image": "assets/مكافحة العناكب.png",
        "intro_ar": "العناكب حشرات مفصلية تفضل الأماكن الهادئة والمظلمة لنسج خيوطها وصيد الحشرات. رغم أن معظم العناكب في مصر غير سامة، إلا أن وجود خيوطها يشوه المظهر الجمالي للمنازل الراقية، ويثير ذعر السكان، كما أن بعض الأنواع تسبب لدغات مؤلمة.",
        "intro_en": "Spiders are predatory arachnids that settle in quiet corners to spin webs. While most domestic species are non-lethal, their webs ruin building aesthetics and trigger arachnophobia, with some species inflicting painful bites.",
        "signs_ar": "تراكم شبكات العنكبوت في زوايا الأسقف، وحول النوافذ، وفي الفراغات المظلمة، ورؤية العناكب تزحف على الجدران ليلاً.",
        "signs_en": "Cobwebs layering ceiling corners, window sills, or basement beams, and visible crawling spiders on walls at night.",
        "risks_ar": "لدغات مؤلمة تسبب تهيج الجلد والتورم، ونادراً ما تحدث مضاعفات سمية، ولكن تكمن خطورتها في التسبب في حالة قلق مستمر ونشر شكل غير نظيف للمكان.",
        "risks_en": "Painful bites leading to localized swelling or skin necrosis in rare cases, alongside triggering constant anxiety for residents.",
        "damage_ar": "تشويه الأسقف الجبسية الفاخرة والديكورات الخارجية بالخيوط والأتربة العالقة بها، وتراكم فضلات الحشرات الميتة في الزوايا.",
        "damage_en": "Staining of expensive gypsum ceilings, stucco facades with dust-laden webs, and build-up of insect carcasses in structural corners.",
        "process_desc_ar": "إزالة خيوط العنكبوت بالكامل بأدوات متخصصة، متبوعاً برش حاجز وقائي طارد طويل الأمد حول النوافذ والأبواب وتحت حواف الأسطح.",
        "process_desc_en": "We physically vacuum/brush away all webs, then spray a micro-encapsulated synthetic pyrethroid barrier on window sills and eaves.",
        "prevention_ar": "تنظيف زوايا المنزل باستمرار بالمكنسة الكهربائية، تركيب شبك حماية ضيق على النوافذ، وتقليل إضاءة الحديقة ليلاً لأنها تجذب الحشرات التي تتغذى عليها العناكب.",
        "prevention_en": "Vacuum ceiling corners regularly, install fine insect screens on windows, and direct outdoor landscaping lights away from walls.",
        "warranty_ar": "ضمان كامل لمدة 6 أشهر يشمل إعادة الخدمة مجاناً في حال ظهور أي شبكات عنكبوت جديدة في الأماكن المعالجة.",
        "warranty_en": "6-month full warranty covering web clearance and free barrier touch-ups if cobwebs return to treated zones.",
        "faq_q1_ar": "هل تقتلون العناكب فقط أم الحشرات التي تتغذى عليها؟",
        "faq_a1_ar": "برنامجنا متكامل؛ فالرش الوقائي يقضي على الحشرات الطائرة والزاحفة الصغيرة، مما يحرم العناكب من مصدر غذائها ويجبرها على مغادرة المكان.",
        "faq_q1_en": "Do you only target spiders or their food source too?",
        "faq_a1_en": "Our barrier spray is multi-action; it eliminates structural flies and moths, cutting off the spiders' food chain to prevent reinvasion.",
        "faq_q2_ar": "هل يمكن رش العناكب في الحدائق المفتوحة؟",
        "faq_a2_ar": "نعم، نقوم برش الأسوار، البرجولات الخشبية، والممرات الخارجية لإنشاء حزام حماية يمنع تسلل العناكب للمنزل.",
        "faq_q2_en": "Can you perform spider treatments on outdoor garden pergolas?",
        "faq_a2_en": "Yes, we treat fences, wooden pergolas, and structural eaves to build a perimeter protective ring shielding the interior.",
        "related_1": "pest-woodborers",
        "related_1_title": "سوس الخشب",
        "related_2": "pest-ants",
        "related_2_title": "النمل"
    }
}

# HTML Template for Pest Pages
pest_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Optimization -->
  <title>{{title_ar}} | {{title_en}} - الشركة الألمانية</title>
  <meta name="description" content="{{meta_desc_ar}}">
  
  <!-- Favicon -->
  <link rel="icon" type="image/jpeg" href="assets/logo.jpg">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=Outfit:wght@300;400;600;700;900&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              deep: '#14532D',
              emerald: '#16A34A',
              charcoal: '#111111',
              dark: '#1E293B',
              light: '#F8FAFC',
            }}
          }}
        }}
      }}
    }}
  </script>
  
  <!-- Custom Stylesheets -->
  <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-brand-light text-brand-dark antialiased">

  {header_html}

  {floating_bar_html}

  <!-- --- 1. DEDICATED PEST HERO SECTION --- -->
  <section class="relative pt-32 pb-20 md:pt-40 md:pb-28 overflow-hidden bg-brand-charcoal text-white">
    <!-- Hero Background with heavy premium overlay -->
    <div class="absolute inset-0 z-0">
      <img src="{{image}}" alt="{{name_en}}" class="w-full h-full object-cover opacity-35 filter brightness-50">
      <div class="absolute inset-0 bg-gradient-to-t from-brand-charcoal via-brand-charcoal/70 to-transparent"></div>
    </div>
    
    <div class="max-w-7xl mx-auto px-6 relative z-10">
      <!-- Back Button -->
      <div class="mb-8 flex">
        <a href="index.html#services" class="inline-flex items-center space-x-2 rtl:space-x-reverse text-slate-300 hover:text-brand-emerald transition-colors font-bold text-sm bg-white/10 backdrop-blur-md border border-white/15 px-5 py-2.5 rounded-xl">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
          </svg>
          <span class="lang-ar">العودة للرئيسية</span>
          <span class="lang-en">Back to Home</span>
        </a>
      </div>

      <!-- Title / Badges -->
      <div class="max-w-4xl text-right rtl:text-right ltr:text-left">
        <div class="inline-flex items-center space-x-2 rtl:space-x-reverse bg-brand-emerald/20 text-brand-emerald border border-brand-emerald/30 px-4 py-1.5 rounded-full text-xs font-bold mb-6">
          <span class="lang-ar">برامج مكافحة الآفات العلمية</span>
          <span class="lang-en">Scientific Pest Control Services</span>
        </div>
        <h1 class="text-4xl md:text-6xl font-black mb-6 leading-tight">
          <span class="lang-ar">بروتوكول إبادة {{name_ar}}</span>
          <span class="lang-en">{{name_en}} Eradication Protocol</span>
        </h1>
        <p class="text-lg md:text-xl text-slate-300 leading-relaxed font-medium mb-8 max-w-3xl">
          <span class="lang-ar">{{intro_ar}}</span>
          <span class="lang-en">{{intro_en}}</span>
        </p>

        <!-- CTAs in Hero -->
        <div class="flex flex-wrap gap-4 justify-start">
          <a href="tel:01033594888" class="px-8 py-4 bg-brand-emerald hover:bg-brand-emerald/90 text-white font-bold rounded-2xl shadow-lg transition-all duration-300 flex items-center space-x-2 rtl:space-x-reverse">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h2.28a1 1 0 01.9.72l.54 2.13a1 1 0 01-.34.98L7.02 7.75a15.91 15.91 0 006.23 6.23l1.15-1.15a1 1 0 01.98-.34l2.13.54a1 1 0 01.72.9V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
            </svg>
            <span class="lang-ar">اتصل بنا الآن</span>
            <span class="lang-en">Call Us Now</span>
          </a>
          <a href="https://wa.me/201033594888" target="_blank" class="px-8 py-4 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-2xl shadow-lg transition-all duration-300 flex items-center space-x-2 rtl:space-x-reverse">
            <span class="lang-ar">واتساب</span>
            <span class="lang-en">WhatsApp Chat</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- --- 2. DETAIL CONTENT GRID --- -->
  <section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        
        <!-- --- Right Column: Main Scientific Details (8 cols) --- -->
        <div class="lg:col-span-8 space-y-16 text-right rtl:text-right ltr:text-left">
          
          <!-- Block 1: Signs & Diagnosis -->
          <div class="space-y-4">
            <h2 class="text-2xl md:text-3xl font-extrabold text-brand-deep flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-1.5 h-8 bg-brand-emerald rounded-full"></span>
              <span class="lang-ar">علامات وجود الإصابة في الموقع</span>
              <span class="lang-en">Signs of Active Infestation</span>
            </h2>
            <p class="text-slate-600 text-base leading-relaxed">
              <span class="lang-ar">{{signs_ar}}</span>
              <span class="lang-en">{{signs_en}}</span>
            </p>
          </div>

          <!-- Block 2: Clinical Risks & Property Damage -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="p-6 bg-red-50/50 rounded-2xl border border-red-100 space-y-3">
              <div class="w-10 h-10 bg-red-100 text-red-600 rounded-xl flex items-center justify-center font-bold">⚠️</div>
              <h3 class="font-bold text-red-950">
                <span class="lang-ar">المخاطر الصحية والسريرية</span>
                <span class="lang-en">Clinical & Health Risks</span>
              </h3>
              <p class="text-red-900/80 text-sm leading-relaxed">
                <span class="lang-ar">{{risks_ar}}</span>
                <span class="lang-en">{{risks_en}}</span>
              </p>
            </div>
            
            <div class="p-6 bg-amber-50/50 rounded-2xl border border-amber-100 space-y-3">
              <div class="w-10 h-10 bg-amber-100 text-amber-600 rounded-xl flex items-center justify-center font-bold">🪵</div>
              <h3 class="font-bold text-amber-950">
                <span class="lang-ar">الأضرار المادية والاقتصادية</span>
                <span class="lang-en">Material & Property Damage</span>
              </h3>
              <p class="text-amber-900/80 text-sm leading-relaxed">
                <span class="lang-ar">{{damage_ar}}</span>
                <span class="lang-en">{{damage_en}}</span>
              </p>
            </div>
          </div>

          <!-- Block 3: Treatment Process Timeline (Inspection, Identification, Treatment, Follow-up, Guarantee) -->
          <div class="space-y-6">
            <h2 class="text-2xl md:text-3xl font-extrabold text-brand-deep flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-1.5 h-8 bg-brand-emerald rounded-full"></span>
              <span class="lang-ar">بروتوكول المعالجة العلمية المعتمد</span>
              <span class="lang-en">Approved Scientific Treatment Protocol</span>
            </h2>
            <p class="text-slate-600 text-sm md:text-base leading-relaxed">
              <span class="lang-ar">نطبق استراتيجية مكافحة من 5 مراحل تتوافق مع بروتوكولات الصحة والبيئة العالمية:</span>
              <span class="lang-en">We follow a rigorous 5-stage Integrated Pest Management (IPM) model:</span>
            </p>

            <!-- Horizontal Timeline / Vertical on Mobile -->
            <div class="relative pl-6 border-l border-slate-200 rtl:border-l-0 rtl:pr-6 rtl:border-r space-y-8">
              
              <!-- Step 1 -->
              <div class="relative">
                <div class="absolute -left-[31px] rtl:-right-[31px] top-1.5 w-4 h-4 rounded-full bg-brand-emerald border-4 border-white shadow"></div>
                <h4 class="font-bold text-brand-deep text-lg">
                  <span class="lang-ar">1. الفحص والمسح الميداني (Inspection)</span>
                  <span class="lang-en">1. Inspection & Mapping</span>
                </h4>
                <p class="text-sm text-slate-500 mt-1">
                  <span class="lang-ar">فحص شامل للهياكل، المفروشات، والشقوق لتحديد بؤر تمركز وتكاثر الحشرة.</span>
                  <span class="lang-en">Thorough onsite audit of crevices, wood structures, and nesting vectors to map infestation size.</span>
                </p>
              </div>

              <!-- Step 2 -->
              <div class="relative">
                <div class="absolute -left-[31px] rtl:-right-[31px] top-1.5 w-4 h-4 rounded-full bg-brand-emerald border-4 border-white shadow"></div>
                <h4 class="font-bold text-brand-deep text-lg">
                  <span class="lang-ar">2. التشخيص وتحديد الفصيلة (Identification)</span>
                  <span class="lang-en">2. Pest Identification</span>
                </h4>
                <p class="text-sm text-slate-500 mt-1">
                  <span class="lang-ar">تحديد سلالة الحشرة بدقة لاختيار المواد الهرمونية والكيميائية الملائمة لمكافحتها.</span>
                  <span class="lang-en">Classifying the specific insect strains to choose targeted biochemical triggers and growth regulators.</span>
                </p>
              </div>

              <!-- Step 3 -->
              <div class="relative">
                <div class="absolute -left-[31px] rtl:-right-[31px] top-1.5 w-4 h-4 rounded-full bg-brand-emerald border-4 border-white shadow"></div>
                <h4 class="font-bold text-brand-deep text-lg">
                  <span class="lang-ar">3. المعالجة الذكية (Treatment)</span>
                  <span class="lang-en">3. Smart Treatment Execution</span>
                </h4>
                <p class="text-sm text-slate-500 mt-1">
                  <span class="lang-ar">{{process_desc_ar}}</span>
                  <span class="lang-en">{{process_desc_en}}</span>
                </p>
              </div>

              <!-- Step 4 -->
              <div class="relative">
                <div class="absolute -left-[31px] rtl:-right-[31px] top-1.5 w-4 h-4 rounded-full bg-brand-emerald border-4 border-white shadow"></div>
                <h4 class="font-bold text-brand-deep text-lg">
                  <span class="lang-ar">4. المتابعة الهندسية (Follow-up)</span>
                  <span class="lang-en">4. Post-Treatment Follow-up</span>
                </h4>
                <p class="text-sm text-slate-500 mt-1">
                  <span class="lang-ar">زيارات تدقيق دورية مجانية لفحص مصائد التتبع والتأكد من عدم ظهور فقس جديد من البيوض.</span>
                  <span class="lang-en">Regular quality control audits and physical sweep checks to guarantee zero late-stage nymph emergence.</span>
                </p>
              </div>

              <!-- Step 5 -->
              <div class="relative">
                <div class="absolute -left-[31px] rtl:-right-[31px] top-1.5 w-4 h-4 rounded-full bg-brand-emerald border-4 border-white shadow"></div>
                <h4 class="font-bold text-brand-deep text-lg">
                  <span class="lang-ar">5. الضمان المعتمد (Guarantee)</span>
                  <span class="lang-en">5. Written Warranty & Guarantee</span>
                </h4>
                <p class="text-sm text-slate-500 mt-1">
                  <span class="lang-ar">{{warranty_ar}}</span>
                  <span class="lang-en">{{warranty_en}}</span>
                </p>
              </div>

            </div>
          </div>

          <!-- Block 4: Prevention & Protection Tips -->
          <div class="space-y-4">
            <h2 class="text-2xl md:text-3xl font-extrabold text-brand-deep flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-1.5 h-8 bg-brand-emerald rounded-full"></span>
              <span class="lang-ar">إرشادات الوقاية من تكرار الإصابة</span>
              <span class="lang-en">Preventive Protocols for Long-term Protection</span>
            </h2>
            <p class="text-slate-600 text-base leading-relaxed">
              <span class="lang-ar">{{prevention_ar}}</span>
              <span class="lang-en">{{prevention_en}}</span>
            </p>
          </div>

          <!-- Block 5: FAQs -->
          <div class="space-y-6">
            <h2 class="text-2xl md:text-3xl font-extrabold text-brand-deep flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-1.5 h-8 bg-brand-emerald rounded-full"></span>
              <span class="lang-ar">الأسئلة الشائعة حول {{name_ar}}</span>
              <span class="lang-en">{{name_en}} Frequently Asked Questions</span>
            </h2>
            
            <div class="space-y-4">
              <!-- Q1 -->
              <div class="bg-brand-light p-5 rounded-2xl border border-slate-100">
                <h4 class="font-bold text-brand-deep mb-2">
                  <span class="lang-ar">❓ {{faq_q1_ar}}</span>
                  <span class="lang-en">❓ {{faq_q1_en}}</span>
                </h4>
                <p class="text-sm text-slate-600 leading-relaxed">
                  <span class="lang-ar">💬 {{faq_a1_ar}}</span>
                  <span class="lang-en">💬 {{faq_a1_en}}</span>
                </p>
              </div>
              <!-- Q2 -->
              <div class="bg-brand-light p-5 rounded-2xl border border-slate-100">
                <h4 class="font-bold text-brand-deep mb-2">
                  <span class="lang-ar">❓ {{faq_q2_ar}}</span>
                  <span class="lang-en">❓ {{faq_q2_en}}</span>
                </h4>
                <p class="text-sm text-slate-600 leading-relaxed">
                  <span class="lang-ar">💬 {{faq_a2_ar}}</span>
                  <span class="lang-en">💬 {{faq_a2_en}}</span>
                </p>
              </div>
            </div>
          </div>

        </div>

        <!-- --- Left Column: Fast Booking & Related (4 cols) --- -->
        <div class="lg:col-span-4 space-y-8 flex flex-col">
          
          <!-- Fast Contact Form -->
          <div class="bg-brand-light p-8 rounded-3xl border border-slate-100 shadow-lg text-right rtl:text-right ltr:text-left space-y-6">
            <div>
              <h3 class="font-black text-brand-deep text-xl mb-1">
                <span class="lang-ar">احجز معالجة فورية</span>
                <span class="lang-en">Book Immediate Service</span>
              </h3>
              <p class="text-slate-500 text-xs">
                <span class="lang-ar">احصل على خصم 15% عند الحجز الإلكتروني اليوم.</span>
                <span class="lang-en">Receive a 15% discount for online bookings.</span>
              </p>
            </div>
            
            <form action="#" class="space-y-4" onsubmit="event.preventDefault(); alert('تم استلام طلبك بنجاح. سيتواصل معك مهندس معتمد فوراً.'); this.reset();">
              <div>
                <label class="block text-xs font-bold text-brand-deep mb-1">
                  <span class="lang-ar">الاسم الكريم *</span><span class="lang-en">Your Name *</span>
                </label>
                <input type="text" required placeholder="أحمد محمد" class="w-full px-3 py-2.5 bg-white border border-slate-200 rounded-xl focus:outline-none focus:border-brand-emerald text-sm transition-colors">
              </div>
              <div>
                <label class="block text-xs font-bold text-brand-deep mb-1">
                  <span class="lang-ar">رقم الهاتف *</span><span class="lang-en">Phone Number *</span>
                </label>
                <input type="tel" required placeholder="0100 000 0000" class="w-full px-3 py-2.5 bg-white border border-slate-200 rounded-xl focus:outline-none focus:border-brand-emerald text-sm transition-colors">
              </div>
              <button type="submit" class="w-full py-3 bg-brand-emerald hover:bg-brand-emerald/90 text-white font-bold rounded-xl text-sm transition-colors shadow">
                <span class="lang-ar">اطلب الخدمة الآن</span>
                <span class="lang-en">Submit Request</span>
              </button>
            </form>
          </div>

          <!-- Hotline Card -->
          <div class="bg-brand-deep text-white p-8 rounded-3xl space-y-4 relative overflow-hidden shadow-lg text-right rtl:text-right ltr:text-left">
            <div class="absolute -right-10 -bottom-10 w-32 h-32 bg-white/5 rounded-full"></div>
            <h4 class="font-bold text-sm text-brand-emerald/80 tracking-widest uppercase">
              <span class="lang-ar">اتصال طارئ (24/7)</span>
              <span class="lang-en">Emergency Call (24/7)</span>
            </h4>
            <div class="space-y-2">
              <p class="text-xs text-slate-300">
                <span class="lang-ar">تحدث مباشرة مع خبير فني لتوجيهك في الخطوات الفورية قبل وصول فريق التعقيم.</span>
                <span class="lang-en">Speak with an onsite supervisor to help you take initial self-isolation actions.</span>
              </p>
              <a href="tel:01033594888" class="text-2xl font-black block hover:text-brand-emerald transition-colors text-white">01033594888</a>
            </div>
          </div>

          <!-- Related Pests -->
          <div class="space-y-4 text-right rtl:text-right ltr:text-left">
            <h3 class="font-extrabold text-brand-deep text-lg">
              <span class="lang-ar">آفات ذات صلة</span>
              <span class="lang-en">Related Pests</span>
            </h3>
            
            <div class="space-y-3">
              <a href="{related_1}.html" class="block p-4 bg-white border border-slate-100 rounded-2xl shadow hover:border-brand-emerald hover:shadow-md transition-all">
                <h4 class="font-bold text-brand-deep text-sm">
                  <span class="lang-ar">{related_1_title}</span>
                  <span class="lang-en">{related_1_title_en}</span>
                </h4>
                <p class="text-[11px] text-slate-400 mt-1">
                  <span class="lang-ar">اضغط لمعاينة تفاصيل دورة الإبادة وضمان الحماية...</span>
                  <span class="lang-en">Click to inspect biological profiles and eradication paths...</span>
                </p>
              </a>
              <a href="{related_2}.html" class="block p-4 bg-white border border-slate-100 rounded-2xl shadow hover:border-brand-emerald hover:shadow-md transition-all">
                <h4 class="font-bold text-brand-deep text-sm">
                  <span class="lang-ar">{related_2_title}</span>
                  <span class="lang-en">{related_2_title_en}</span>
                </h4>
                <p class="text-[11px] text-slate-400 mt-1">
                  <span class="lang-ar">اضغط لمعاينة تفاصيل دورة الإبادة وضمان الحماية...</span>
                  <span class="lang-en">Click to inspect biological profiles and eradication paths...</span>
                </p>
              </a>
            </div>
          </div>

        </div>

      </div>
    </div>
  </section>

  <!-- --- 3. COMMON DUAL CTA BANNER --- -->
  <section class="py-16 bg-brand-charcoal text-white relative overflow-hidden">
    <div class="absolute inset-0 bg-brand-emerald/10 z-0"></div>
    <div class="max-w-5xl mx-auto px-6 text-center relative z-10 space-y-8">
      <h2 class="text-3xl md:text-4xl font-extrabold leading-tight">
        <span class="lang-ar">هل تعاني من انتشار {{name_ar}} في منشأتك؟</span>
        <span class="lang-en">Struggling with {{name_en}} at Your Property?</span>
      </h2>
      <p class="text-slate-300 text-sm md:text-base max-w-2xl mx-auto">
        <span class="lang-ar">لا تدع الآفات تهدد صحة عائلتك أو عملاء عملك التجاري. فريقنا الفني مجهز بأحدث المعدات الألمانية والمبيدات العضوية الآمنة تماماً. اتصل بنا الآن للحصول على فحص ميداني شامل.</span>
        <span class="lang-en">Don't compromise your family's health or brand safety. Our certified engineering staff is ready with bio-rational products and safe spray barriers. Book a professional inspection today.</span>
      </p>
      <div class="flex flex-wrap justify-center gap-4">
        <a href="tel:01033594888" class="px-8 py-4 bg-brand-emerald hover:bg-brand-emerald/90 text-white font-bold rounded-2xl shadow-lg transition-all duration-300 flex items-center space-x-2 rtl:space-x-reverse">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h2.28a1 1 0 01.9.72l.54 2.13a1 1 0 01-.34.98L7.02 7.75a15.91 15.91 0 006.23 6.23l1.15-1.15a1 1 0 01.98-.34l2.13.54a1 1 0 01.72.9V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
          </svg>
          <span class="lang-ar">اتصل بخبير الفحص</span>
          <span class="lang-en">Call Technical Expert</span>
        </a>
        <a href="https://wa.me/201033594888" target="_blank" class="px-8 py-4 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-2xl shadow-lg transition-all duration-300">
          <span class="lang-ar">محادثة واتساب الفورية</span>
          <span class="lang-en">Instant WhatsApp Chat</span>
        </a>
      </div>
    </div>
  </section>

  {footer_html}

  <!-- Javascript assets -->
  <script src="app.js"></script>
</body>
</html>
"""

# Map names for related English links
names_map = {
    "pest-bedbugs": "Bed Bugs",
    "pest-cockroaches": "Cockroaches",
    "pest-termites": "Termites",
    "pest-woodborers": "Wood Borers",
    "pest-ants": "Ants",
    "pest-mosquitoes": "Mosquitoes",
    "pest-flies": "Flies",
    "pest-fleas": "Fleas",
    "pest-rodents": "Rodents",
    "pest-spiders": "Spiders"
}

# Write pages
for pest_id, data in pests_data.items():
    # Populate related values
    r1 = data["related_1"]
    r2 = data["related_2"]
    
    html_content = (
        pest_template.replace("{{title_ar}}", data["title_ar"])
        .replace("{{title_en}}", data["title_en"])
        .replace("{{meta_desc_ar}}", data["meta_desc_ar"])
        .replace("{{meta_desc_en}}", data["meta_desc_en"])
        .replace("{{name_ar}}", data["name_ar"])
        .replace("{{name_en}}", data["name_en"])
        .replace("{{image}}", data["image"])
        .replace("{{intro_ar}}", data["intro_ar"])
        .replace("{{intro_en}}", data["intro_en"])
        .replace("{{signs_ar}}", data["signs_ar"])
        .replace("{{signs_en}}", data["signs_en"])
        .replace("{{risks_ar}}", data["risks_ar"])
        .replace("{{risks_en}}", data["risks_en"])
        .replace("{{damage_ar}}", data["damage_ar"])
        .replace("{{damage_en}}", data["damage_en"])
        .replace("{{process_desc_ar}}", data["process_desc_ar"])
        .replace("{{process_desc_en}}", data["process_desc_en"])
        .replace("{{prevention_ar}}", data["prevention_ar"])
        .replace("{{prevention_en}}", data["prevention_en"])
        .replace("{{warranty_ar}}", data["warranty_ar"])
        .replace("{{warranty_en}}", data["warranty_en"])
        .replace("{{faq_q1_ar}}", data["faq_q1_ar"])
        .replace("{{faq_a1_ar}}", data["faq_a1_ar"])
        .replace("{{faq_q1_en}}", data["faq_q1_en"])
        .replace("{{faq_a1_en}}", data["faq_a1_en"])
        .replace("{{faq_q2_ar}}", data["faq_q2_ar"])
        .replace("{{faq_a2_ar}}", data["faq_a2_ar"])
        .replace("{{faq_q2_en}}", data["faq_q2_en"])
        .replace("{{faq_a2_en}}", data["faq_a2_en"])
    )
    
    html_content = html_content.format(
        related_1=r1,
        related_1_title=data["related_1_title"],
        related_1_title_en=names_map[r1],
        related_2=r2,
        related_2_title=data["related_2_title"],
        related_2_title_en=names_map[r2],
        header_html=header_html,
        floating_bar_html=floating_bar_html,
        footer_html=footer_html
    )
    
    filename = f"{pest_id}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated: {filename}")
