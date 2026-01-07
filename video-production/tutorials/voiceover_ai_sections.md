# AI Voice Generation - Script Sections
## Optimized for ElevenLabs or Similar AI Voice Services

**Voice Recommendation**: ElevenLabs "Adam" (Australian accent)
**Settings**: Stability: 0.5, Clarity: 0.75, Style Exaggeration: 0.25

---

## SECTION 1: INTRO (0:00 - 0:30)
**Filename**: `01_intro.mp3`
**Duration**: ~30 seconds

G'day everyone! Today I'm going to show you how I built my entire professional portfolio website using Claude AI - no traditional coding required.

If you've been thinking about creating your own portfolio site but you're not a web developer, or if you're curious about how AI can help you build production-quality websites, you're in the right place.

By the end of this tutorial, you'll know exactly how to collaborate with Claude to create a stunning, responsive website and host it for free on GitHub Pages. Let's dive in!

---

## SECTION 2: PLANNING (0:30 - 2:00)
**Filename**: `02_planning.mp3`
**Duration**: ~90 seconds

Before jumping into Claude, I spent some time thinking about what I wanted to achieve. This is crucial - Claude works best when you've got clear goals in mind.

Here's what I sorted out first:

Purpose: I needed a professional portfolio to showcase my data engineering experience, technical skills, and projects. Think of it as my digital CV that actually looks good.

Content: I made a list of what I wanted to include - an about section, my technical stack, work experience, featured projects, certifications, education, and a contact form. I also gathered all my content ahead of time: job descriptions, project details, and certification information.

Design inspiration: I looked at a few portfolio sites I liked and took screenshots. Not to copy them, but to identify what aesthetics appealed to me. I wanted something clean, professional, but with a bit of personality.

Technical requirements: I knew I wanted it to be a single-page site with smooth scrolling navigation, fully responsive across devices, and easy to host for free.

Pro tip: The better your brief to Claude, the better your results. Don't just say "make me a website" - be specific about your goals, audience, and preferences.

---

## SECTION 3: FIRST CONVERSATION (2:00 - 4:00)
**Filename**: `03_first_conversation.mp3`
**Duration**: ~120 seconds

Now here's where it gets interesting. I opened up Claude and started with a detailed prompt. Here's roughly what I said:

"I want to build a professional portfolio website for my data engineering career. I need a single-page site with smooth scrolling navigation. Sections should include: About Me, Technical Stack, Experience, Projects, Certifications, Education, and Contact. I want a modern, clean design that works perfectly on mobile and desktop. Can you help me build this?"

And here's the brilliant thing - Claude immediately understood the scope and started asking clarifying questions: What colour scheme did I prefer? Did I want any animations or interactive elements? What was my preferred style - minimal, bold, corporate, creative?

I responded with my preferences: I wanted a professional look with a clean colour palette - blues and whites with some subtle gradients. I wanted smooth animations but nothing over the top. And I definitely needed a fixed navigation bar.

Claude then created the initial HTML, CSS, and JavaScript files. It built out the complete structure: A header with navigation, all my sections with placeholder content, responsive CSS with media queries, smooth scrolling functionality, and a contact form.

The first version wasn't perfect, but it was a solid starting point - probably 70% of the way there. This is normal and expected!

---

## SECTION 4: ITERATIVE REFINEMENT (4:00 - 7:30)
**Filename**: `04_iteration.mp3`
**Duration**: ~210 seconds

This is where the real magic happens. Building a website with Claude isn't a one-shot deal - it's an iterative conversation. Here's how I refined it:

Round 1 - Content Population. I started copying in my actual content - my bio, job descriptions, project details. As I did this, I noticed the sections needed better spacing and hierarchy. I told Claude: "The experience section feels cramped. Can you increase the spacing between jobs and make the company names more prominent?" Claude updated the CSS immediately, adjusting margins, padding, and font weights.

Round 2 - Visual Refinement. I then focused on aesthetics. The colour scheme was good but needed tweaking. "Can you adjust the header background to be a darker shade of blue? And let's add a subtle gradient overlay to the hero section." Claude made those changes and suggested adding a gradient to the skills cards as well, which looked fantastic.

Round 3 - Technical Stack Section. The skills section was just a boring list. I wanted something more visual. "Let's display the technical stack as cards with icons. Group them into categories: Platforms & Tools, Languages, Architecture, and Methodologies." Claude restructured the entire section, created styled cards with subtle hover effects, and organized everything into a clean grid layout.

Round 4 - Responsive Design Issues. When I tested on my phone, the navigation menu wasn't working properly on mobile. "The nav menu needs to be a hamburger menu on mobile devices with a slide-out drawer." Claude implemented a complete mobile menu with smooth animations and a working toggle button.

Round 5 - Interactive Elements. I wanted the site to feel more dynamic. "Can you add smooth fade-in animations as I scroll down the page? And make the project cards have a subtle lift effect on hover?" Claude added intersection observer JavaScript for scroll animations and enhanced the CSS with transform effects.

Round 6 - Contact Form Functionality. The contact form was just HTML with no backend. I asked Claude how to make it functional without setting up a server. Claude suggested using Formspree - a free form handling service - and updated the form with the proper action attribute and method. Now emails come straight to my inbox.

Key Lesson: Don't be afraid to be specific about what you want changed. Claude responds well to direct feedback like "make this bigger," "change this colour," "add spacing here."

---

## SECTION 5: ADDING POLISH (7:30 - 9:30)
**Filename**: `05_polish.mp3`
**Duration**: ~120 seconds

Once the core structure was solid, I focused on those little details that make a website feel professional:

Favicon and Meta Tags. I asked Claude to add proper meta tags for SEO and social media sharing. I also uploaded a profile photo and asked Claude to help me create a favicon.

Typography Refinement. The default fonts were fine, but I wanted something with more character. I asked Claude to recommend Google Fonts that would suit a professional tech portfolio. We settled on a combination that felt modern but readable.

Micro-interactions. I wanted subtle details that make the site feel polished: Button hover states with smooth transitions, a "back to top" button that appears when scrolling, and active state highlighting in the navigation.

Accessibility. This is something I almost forgot! I asked Claude to review the site for accessibility and it added: Proper ARIA labels, keyboard navigation support, sufficient color contrast ratios, and alt text for images.

Performance Optimization. Finally, I asked Claude about performance. It suggested: Minifying the CSS, using loading="lazy" for images, and removing any unused CSS.

---

## SECTION 6: GITHUB PAGES (9:30 - 11:30)
**Filename**: `06_deployment.mp3`
**Duration**: ~120 seconds

Right, so now I had a fully functional website, but it was just sitting on my computer. Time to get it online with GitHub Pages - completely free hosting.

Step 1: Create a GitHub Repository. I went to GitHub and created a new repository. Important: I named it bradcoles-dev.github.io - that's my username followed by .github.io. This is crucial for GitHub Pages to work as your main site.

Step 2: Upload the Files. I uploaded my HTML file - renamed to index.html - my CSS file, JavaScript file, and images folder to the repository. You can do this through the GitHub web interface or use Git commands if you're comfortable with that.

Step 3: Enable GitHub Pages. In the repository settings, I scrolled down to the "Pages" section and selected the main branch as the source. GitHub then automatically deployed the site.

Within a couple of minutes, my site was live at bradcoles-dev.github.io

Step 4: Custom Domain - Optional. If you want to use your own domain name instead of the .github.io URL, you can add a custom domain in the same Pages settings. You'll need to configure DNS settings with your domain registrar, but Claude can walk you through that process if needed.

Pro Tip: Any time you update your files in the GitHub repository, GitHub Pages automatically redeploys your site. It's a brilliant workflow for making updates.

---

## SECTION 7: TIPS FOR SUCCESS (11:30 - 13:00)
**Filename**: `07_tips.mp3`
**Duration**: ~90 seconds

After building this entire site with Claude, here are my top tips:

Number 1: Be Specific in Your Requests. Instead of "Make it look better", try "Increase the spacing between sections to 80 pixels and make the heading font size larger"

Number 2: Iterate in Small Steps. Don't try to get everything perfect in one go. Make one change, review it, then move to the next. This makes it easier to catch issues early.

Number 3: Ask for Explanations. If Claude does something you don't understand, ask! "Why did you use flexbox here instead of grid?" Claude is excellent at explaining its decisions, which helps you learn.

Number 4: Provide Visual Feedback. If you can, take screenshots of issues and describe them. "The mobile menu overlaps with the logo" is much clearer than "the mobile version is broken."

Number 5: Use Claude for Problem-Solving. When you hit a snag, describe the problem rather than trying to solve it yourself. "The images are loading slowly" - Claude might suggest image optimization techniques you hadn't considered.

Number 6: Test Thoroughly. Claude can't see your browser, so you need to be the tester. Check on different devices, different browsers, and different screen sizes.

---

## SECTION 8: LIMITATIONS (13:00 - 14:00)
**Filename**: `08_limitations.mp3`
**Duration**: ~60 seconds

Claude is incredibly powerful, but there are limits to what you should expect:

What Claude Does Brilliantly: Creating HTML, CSS, and JavaScript, implementing responsive design, adding animations and interactions, structuring content logically, debugging code issues, and explaining technical concepts.

Where You Might Need Additional Help: Complex backend functionality like databases and user authentication, advanced hosting configurations, complex form processing beyond simple email, e-commerce functionality, and very specific browser compatibility issues.

For my portfolio site, Claude handled everything I needed. But if you're building something more complex - like a web application with user accounts and databases - you'll likely need to combine Claude's help with other development resources or tools.

The Good News: For portfolio sites, landing pages, business websites, and most informational sites, Claude can handle the entire build.

---

## SECTION 9: OUTRO (14:00 - 14:45)
**Filename**: `09_outro.mp3`
**Duration**: ~45 seconds

So there you have it! I built a complete, professional portfolio website using Claude AI - no coding background required. The entire process took me about 4 to 5 hours from start to finish, including content gathering, design iterations, and deployment.

Here's what made this successful: Clear planning before starting, specific detailed prompts to Claude, iterative refinement through conversation, thorough testing across devices, and free hosting with GitHub Pages.

If you're thinking about building your own site, I reckon this is the perfect time to dive in. AI tools like Claude have genuinely democratized web development - you don't need to be a coder anymore to have a professional online presence.

I'd love to see what you build! Drop a link to your portfolio in the comments below. And if you run into any issues, feel free to ask - I'm happy to help troubleshoot.

If you found this tutorial helpful, don't forget to like, subscribe, and hit that notification bell. I'll be creating more content about using AI tools for practical projects.

Thanks for watching, and good luck building your site!

Cheers!

---

## GENERATION INSTRUCTIONS

### For ElevenLabs:
1. Go to https://elevenlabs.io
2. Select "Adam" voice (Australian accent)
3. Settings: Stability: 0.5, Clarity: 0.75
4. Copy each section above (excluding the filename and duration)
5. Generate audio for each section
6. Download as MP3 with the suggested filename

### For Play.ht:
1. Go to https://play.ht
2. Select "Matthew" or "Australian English Male"
3. Copy each section above
4. Generate and download with suggested filenames

### For Murf.ai:
1. Go to https://murf.ai
2. Select Australian accent voice
3. Copy each section above
4. Generate and download with suggested filenames

### Quality Check:
- Listen to each section for natural pacing
- Ensure no robotic pronunciation
- Check that pauses feel natural
- Re-generate any awkward sections

### Total Duration: ~14 minutes 45 seconds
