# Building a Professional Portfolio Website with Claude - Voiceover Script
## YouTube Tutorial | Duration: ~12-15 minutes

---

## INTRO (0:00 - 0:30)

G'day everyone! Today I'm going to show you how I built my entire professional portfolio website using Claude AI - no traditional coding required. 

If you've been thinking about creating your own portfolio site but you're not a web developer, or if you're curious about how AI can help you build production-quality websites, you're in the right place.

By the end of this tutorial, you'll know exactly how to collaborate with Claude to create a stunning, responsive website and host it for free on GitHub Pages. Let's dive in!

---

## PART 1: PLANNING & SETUP (0:30 - 2:00)

**The Foundation**

Before jumping into Claude, I spent some time thinking about what I wanted to achieve. This is crucial - Claude works best when you've got clear goals in mind.

Here's what I sorted out first:

**Purpose**: I needed a professional portfolio to showcase my data engineering experience, technical skills, and projects. Think of it as my digital CV that actually looks good.

**Content**: I made a list of what I wanted to include - an about section, my technical stack, work experience, featured projects, certifications, education, and a contact form. I also gathered all my content ahead of time: job descriptions, project details, and certification information.

**Design inspiration**: I looked at a few portfolio sites I liked and took screenshots. Not to copy them, but to identify what aesthetics appealed to me. I wanted something clean, professional, but with a bit of personality.

**Technical requirements**: I knew I wanted it to be a single-page site with smooth scrolling navigation, fully responsive across devices, and easy to host for free.

**Pro tip**: The better your brief to Claude, the better your results. Don't just say "make me a website" - be specific about your goals, audience, and preferences.

---

## PART 2: FIRST CONVERSATION WITH CLAUDE (2:00 - 4:00)

**Starting the Collaboration**

Now here's where it gets interesting. I opened up Claude and started with a detailed prompt. Here's roughly what I said:

"I want to build a professional portfolio website for my data engineering career. I need a single-page site with smooth scrolling navigation. Sections should include: About Me, Technical Stack, Experience, Projects, Certifications, Education, and Contact. I want a modern, clean design that works perfectly on mobile and desktop. Can you help me build this?"

And here's the brilliant thing - Claude immediately understood the scope and started asking clarifying questions:
- What colour scheme did I prefer?
- Did I want any animations or interactive elements?
- What was my preferred style - minimal, bold, corporate, creative?

I responded with my preferences: I wanted a professional look with a clean colour palette - blues and whites with some subtle gradients. I wanted smooth animations but nothing over the top. And I definitely needed a fixed navigation bar.

**The First Draft**

Claude then created the initial HTML, CSS, and JavaScript files. It built out the complete structure:
- A header with navigation
- All my sections with placeholder content
- Responsive CSS with media queries
- Smooth scrolling functionality
- A contact form

The first version wasn't perfect, but it was a solid starting point - probably 70% of the way there. This is normal and expected!

---

## PART 3: ITERATIVE REFINEMENT (4:00 - 7:30)

**The Back-and-Forth Process**

This is where the real magic happens. Building a website with Claude isn't a one-shot deal - it's an iterative conversation. Here's how I refined it:

**Round 1 - Content Population**

I started copying in my actual content - my bio, job descriptions, project details. As I did this, I noticed the sections needed better spacing and hierarchy.

I told Claude: "The experience section feels cramped. Can you increase the spacing between jobs and make the company names more prominent?"

Claude updated the CSS immediately, adjusting margins, padding, and font weights.

**Round 2 - Visual Refinement**

I then focused on aesthetics. The colour scheme was good but needed tweaking.

"Can you adjust the header background to be a darker shade of blue? And let's add a subtle gradient overlay to the hero section."

Claude made those changes and suggested adding a gradient to the skills cards as well, which looked fantastic.

**Round 3 - Technical Stack Section**

The skills section was just a boring list. I wanted something more visual.

"Let's display the technical stack as cards with icons. Group them into categories: Platforms & Tools, Languages, Architecture, and Methodologies."

Claude restructured the entire section, created styled cards with subtle hover effects, and organized everything into a clean grid layout.

**Round 4 - Responsive Design Issues**

When I tested on my phone, the navigation menu wasn't working properly on mobile.

"The nav menu needs to be a hamburger menu on mobile devices with a slide-out drawer."

Claude implemented a complete mobile menu with smooth animations and a working toggle button.

**Round 5 - Interactive Elements**

I wanted the site to feel more dynamic.

"Can you add smooth fade-in animations as I scroll down the page? And make the project cards have a subtle lift effect on hover?"

Claude added intersection observer JavaScript for scroll animations and enhanced the CSS with transform effects.

**Round 6 - Contact Form Functionality**

The contact form was just HTML with no backend. I asked Claude how to make it functional without setting up a server.

Claude suggested using Formspree (a free form handling service) and updated the form with the proper action attribute and method. Now emails come straight to my inbox.

**Key Lesson**: Don't be afraid to be specific about what you want changed. Claude responds well to direct feedback like "make this bigger," "change this colour," "add spacing here."

---

## PART 4: ADDING POLISH & PERSONALITY (7:30 - 9:30)

**The Final Touches**

Once the core structure was solid, I focused on those little details that make a website feel professional:

**Favicon and Meta Tags**

I asked Claude to add proper meta tags for SEO and social media sharing. I also uploaded a profile photo and asked Claude to help me create a favicon.

**Typography Refinement**

The default fonts were fine, but I wanted something with more character. I asked Claude to recommend Google Fonts that would suit a professional tech portfolio. We settled on a combination that felt modern but readable.

**Micro-interactions**

I wanted subtle details that make the site feel polished:
- Button hover states with smooth transitions
- A "back to top" button that appears when scrolling
- Active state highlighting in the navigation

**Accessibility**

This is something I almost forgot! I asked Claude to review the site for accessibility and it added:
- Proper ARIA labels
- Keyboard navigation support
- Sufficient color contrast ratios
- Alt text for images

**Performance Optimization**

Finally, I asked Claude about performance. It suggested:
- Minifying the CSS
- Using loading="lazy" for images
- Removing any unused CSS

---

## PART 5: GITHUB PAGES DEPLOYMENT (9:30 - 11:30)

**Getting It Online**

Right, so now I had a fully functional website, but it was just sitting on my computer. Time to get it online with GitHub Pages - completely free hosting.

**Step 1: Create a GitHub Repository**

I went to GitHub and created a new repository. Important: I named it `bradcoles-dev.github.io` - that's my username followed by `.github.io`. This is crucial for GitHub Pages to work as your main site.

**Step 2: Upload the Files**

I uploaded my HTML file (renamed to `index.html`), my CSS file, JavaScript file, and images folder to the repository. You can do this through the GitHub web interface or use Git commands if you're comfortable with that.

**Step 3: Enable GitHub Pages**

In the repository settings, I scrolled down to the "Pages" section and selected the main branch as the source. GitHub then automatically deployed the site.

Within a couple of minutes, my site was live at `https://bradcoles-dev.github.io/`

**Step 4: Custom Domain (Optional)**

If you want to use your own domain name instead of the `.github.io` URL, you can add a custom domain in the same Pages settings. You'll need to configure DNS settings with your domain registrar, but Claude can walk you through that process if needed.

**Pro Tip**: Any time you update your files in the GitHub repository, GitHub Pages automatically redeploys your site. It's a brilliant workflow for making updates.

---

## PART 6: TIPS FOR WORKING WITH CLAUDE (11:30 - 13:00)

**What I Learned**

After building this entire site with Claude, here are my top tips:

**1. Be Specific in Your Requests**

Instead of: "Make it look better"
Try: "Increase the spacing between sections to 80px and make the heading font size larger"

**2. Iterate in Small Steps**

Don't try to get everything perfect in one go. Make one change, review it, then move to the next. This makes it easier to catch issues early.

**3. Ask for Explanations**

If Claude does something you don't understand, ask! "Why did you use flexbox here instead of grid?" Claude is excellent at explaining its decisions, which helps you learn.

**4. Provide Visual Feedback**

If you can, take screenshots of issues and describe them. "The mobile menu overlaps with the logo" is much clearer than "the mobile version is broken."

**5. Use Claude for Problem-Solving**

When you hit a snag, describe the problem rather than trying to solve it yourself. "The images are loading slowly" - Claude might suggest image optimization techniques you hadn't considered.

**6. Keep the Conversation Organized**

For major changes, it helps to start a new chat with Claude and provide context: "I'm working on a portfolio website. Previously, we built sections A, B, and C. Now I need to add section D."

**7. Reference Best Practices**

Ask Claude about best practices: "What's the best way to structure this for SEO?" or "How should I handle responsive images?"

**8. Test Thoroughly**

Claude can't see your browser, so you need to be the tester. Check on different devices, different browsers, and different screen sizes.

---

## PART 7: LIMITATIONS & WHEN TO SEEK HELP (13:00 - 14:00)

**Being Realistic**

Claude is incredibly powerful, but there are limits to what you should expect:

**What Claude Does Brilliantly:**
- Creating HTML, CSS, and JavaScript
- Implementing responsive design
- Adding animations and interactions
- Structuring content logically
- Debugging code issues
- Explaining technical concepts

**Where You Might Need Additional Help:**
- Complex backend functionality (databases, user authentication)
- Advanced hosting configurations
- Complex form processing beyond simple email
- E-commerce functionality
- Very specific browser compatibility issues

For my portfolio site, Claude handled everything I needed. But if you're building something more complex - like a web application with user accounts and databases - you'll likely need to combine Claude's help with other development resources or tools.

**The Good News**: For portfolio sites, landing pages, business websites, and most informational sites, Claude can handle the entire build.

---

## OUTRO (14:00 - 14:45)

**Wrapping Up**

So there you have it! I built a complete, professional portfolio website using Claude AI - no coding background required. The entire process took me about 4-5 hours from start to finish, including content gathering, design iterations, and deployment.

Here's what made this successful:
- Clear planning before starting
- Specific, detailed prompts to Claude
- Iterative refinement through conversation
- Thorough testing across devices
- Free hosting with GitHub Pages

If you're thinking about building your own site, I reckon this is the perfect time to dive in. AI tools like Claude have genuinely democratized web development - you don't need to be a coder anymore to have a professional online presence.

**What's Next?**

I'd love to see what you build! Drop a link to your portfolio in the comments below. And if you run into any issues, feel free to ask - I'm happy to help troubleshoot.

If you found this tutorial helpful, don't forget to like, subscribe, and hit that notification bell. I'll be creating more content about using AI tools for practical projects.

Thanks for watching, and good luck building your site!

Cheers!

---

## NOTES FOR RECORDING

**Tone**: Friendly, conversational, knowledgeable but not condescending. Speak as if explaining to a mate who's interested but not technical.

**Pacing**: Don't rush. Pause between major sections. Speak clearly - this is educational content.

**Australian Terms Used**:
- "G'day" (opening)
- "sorted out" instead of "figured out"
- "brilliant" instead of "great/amazing"
- "I reckon" instead of "I think"
- "mate" (casual reference)
- "Cheers" (closing)

**Screen Recording Recommendations**:
- Show the Claude interface during Parts 2-4
- Screen capture the website at various stages
- Show mobile responsive testing
- Demonstrate the GitHub Pages deployment process
- Show the final live website

**Visual Overlay Suggestions**:
- Text overlays for key tips
- Arrow annotations pointing to specific elements
- Before/after comparisons for changes
- Split-screen showing prompt and result

**Background Music**: Consider subtle, upbeat background music at low volume (royalty-free options from YouTube Audio Library or Epidemic Sound)
