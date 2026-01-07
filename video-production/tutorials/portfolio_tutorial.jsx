import React, { useState, useEffect } from 'react';
import { ChevronLeft, ChevronRight, Home, Code, Sparkles, Rocket, Settings, Check, Github, Globe, MessageSquare, Lightbulb, AlertCircle, Monitor, Smartphone } from 'lucide-react';

export default function PortfolioTutorial() {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    setProgress((currentSlide / (slides.length - 1)) * 100);
  }, [currentSlide]);

  const slides = [
    {
      id: 'intro',
      title: 'Building a Professional Portfolio',
      subtitle: 'With Claude AI',
      type: 'cover',
      icon: <Sparkles className="w-24 h-24" />,
      content: (
        <div className="text-center space-y-6">
          <p className="text-2xl font-light">From Idea to Deployment</p>
          <p className="text-lg opacity-80">No coding experience required</p>
          <div className="flex justify-center gap-4 mt-8">
            <div className="bg-white/10 backdrop-blur px-6 py-3 rounded-full">
              <span className="text-sm">⏱️ 12-15 minutes</span>
            </div>
            <div className="bg-white/10 backdrop-blur px-6 py-3 rounded-full">
              <span className="text-sm">🎯 Beginner Friendly</span>
            </div>
          </div>
        </div>
      )
    },
    {
      id: 'planning',
      title: 'Step 1: Planning',
      subtitle: 'Foundation is Everything',
      type: 'content',
      icon: <Settings className="w-16 h-16" />,
      content: (
        <div className="space-y-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-gradient-to-br from-blue-500/20 to-purple-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-3">
                <span className="bg-blue-500 w-8 h-8 rounded-full flex items-center justify-center text-sm">1</span>
                Define Purpose
              </h3>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• Who is this for?</li>
                <li>• What do you want to achieve?</li>
                <li>• What makes you unique?</li>
              </ul>
            </div>
            
            <div className="bg-gradient-to-br from-purple-500/20 to-pink-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-3">
                <span className="bg-purple-500 w-8 h-8 rounded-full flex items-center justify-center text-sm">2</span>
                Gather Content
              </h3>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• Work experience details</li>
                <li>• Project descriptions</li>
                <li>• Skills & certifications</li>
              </ul>
            </div>
            
            <div className="bg-gradient-to-br from-pink-500/20 to-red-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-3">
                <span className="bg-pink-500 w-8 h-8 rounded-full flex items-center justify-center text-sm">3</span>
                Design Inspiration
              </h3>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• Browse portfolio sites</li>
                <li>• Identify aesthetics you like</li>
                <li>• Save screenshots for reference</li>
              </ul>
            </div>
            
            <div className="bg-gradient-to-br from-red-500/20 to-orange-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
              <h3 className="text-xl font-bold mb-4 flex items-center gap-3">
                <span className="bg-red-500 w-8 h-8 rounded-full flex items-center justify-center text-sm">4</span>
                Technical Goals
              </h3>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• Single page or multi-page?</li>
                <li>• Mobile responsive?</li>
                <li>• Contact form needed?</li>
              </ul>
            </div>
          </div>
          
          <div className="bg-yellow-500/20 backdrop-blur border-l-4 border-yellow-500 p-4 rounded-r-lg">
            <p className="text-sm font-semibold flex items-center gap-2">
              <Lightbulb className="w-5 h-5" />
              Pro Tip: Better brief = Better results
            </p>
          </div>
        </div>
      )
    },
    {
      id: 'first-prompt',
      title: 'Step 2: First Conversation',
      subtitle: 'Crafting Your Initial Prompt',
      type: 'content',
      icon: <MessageSquare className="w-16 h-16" />,
      content: (
        <div className="space-y-6">
          <div className="bg-gradient-to-br from-indigo-600/30 to-blue-600/30 backdrop-blur p-8 rounded-2xl border border-white/20">
            <div className="flex items-start gap-4 mb-4">
              <div className="bg-white/20 p-3 rounded-full">
                <Code className="w-6 h-6" />
              </div>
              <div className="flex-1">
                <h3 className="text-xl font-bold mb-3">Example Initial Prompt</h3>
                <div className="bg-black/30 p-6 rounded-xl font-mono text-sm leading-relaxed">
                  <p className="text-green-400">"I want to build a professional portfolio website for my data engineering career.</p>
                  <p className="mt-2">I need a single-page site with smooth scrolling navigation.</p>
                  <p className="mt-2">Sections: About Me, Technical Stack, Experience, Projects, Certifications, Education, Contact.</p>
                  <p className="mt-2">Modern, clean design. Must work on mobile and desktop.</p>
                  <p className="mt-2 text-green-400">Can you help me build this?"</p>
                </div>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-white/5 backdrop-blur p-5 rounded-xl border border-emerald-500/30">
              <h4 className="font-bold mb-2 text-emerald-400">Be Specific</h4>
              <p className="text-sm opacity-80">Include sections, style preferences, functionality</p>
            </div>
            <div className="bg-white/5 backdrop-blur p-5 rounded-xl border border-blue-500/30">
              <h4 className="font-bold mb-2 text-blue-400">Set Expectations</h4>
              <p className="text-sm opacity-80">Mention responsive design, animations, interactivity</p>
            </div>
            <div className="bg-white/5 backdrop-blur p-5 rounded-xl border border-purple-500/30">
              <h4 className="font-bold mb-2 text-purple-400">Stay Open</h4>
              <p className="text-sm opacity-80">Let Claude ask clarifying questions</p>
            </div>
          </div>

          <div className="bg-white/5 backdrop-blur p-6 rounded-xl">
            <h4 className="font-bold mb-3 flex items-center gap-2">
              <Check className="w-5 h-5 text-green-400" />
              What Happens Next
            </h4>
            <ul className="space-y-2 text-sm opacity-90">
              <li>✓ Claude asks about color schemes and style preferences</li>
              <li>✓ Clarifies technical requirements</li>
              <li>✓ Generates complete HTML, CSS, and JavaScript files</li>
              <li>✓ Creates ~70% complete first draft</li>
            </ul>
          </div>
        </div>
      )
    },
    {
      id: 'iteration',
      title: 'Step 3: Iterative Refinement',
      subtitle: 'The Magic Happens Here',
      type: 'content',
      icon: <Sparkles className="w-16 h-16" />,
      content: (
        <div className="space-y-6">
          <p className="text-lg opacity-90">Building with Claude is a conversation, not a one-shot process</p>
          
          <div className="space-y-4">
            {[
              { round: 1, title: 'Content Population', desc: 'Add real content, adjust spacing & hierarchy', color: 'from-cyan-500/20 to-blue-500/20' },
              { round: 2, title: 'Visual Refinement', desc: 'Tweak colors, add gradients, adjust fonts', color: 'from-blue-500/20 to-indigo-500/20' },
              { round: 3, title: 'Component Enhancement', desc: 'Transform lists into cards, add icons', color: 'from-indigo-500/20 to-purple-500/20' },
              { round: 4, title: 'Responsive Design', desc: 'Fix mobile issues, implement hamburger menu', color: 'from-purple-500/20 to-pink-500/20' },
              { round: 5, title: 'Interactive Elements', desc: 'Add animations, hover effects, transitions', color: 'from-pink-500/20 to-red-500/20' },
              { round: 6, title: 'Functionality', desc: 'Connect contact form, add real features', color: 'from-red-500/20 to-orange-500/20' }
            ].map((round) => (
              <div key={round.round} className={`bg-gradient-to-r ${round.color} backdrop-blur p-5 rounded-xl border border-white/10 transform hover:scale-105 transition-transform`}>
                <div className="flex items-center gap-4">
                  <div className="bg-white/20 w-12 h-12 rounded-full flex items-center justify-center font-bold text-xl">
                    {round.round}
                  </div>
                  <div className="flex-1">
                    <h4 className="font-bold text-lg">{round.title}</h4>
                    <p className="text-sm opacity-80">{round.desc}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="bg-amber-500/20 backdrop-blur border-l-4 border-amber-500 p-4 rounded-r-lg">
            <p className="text-sm font-semibold flex items-center gap-2">
              <AlertCircle className="w-5 h-5" />
              Key Lesson: Be specific with feedback. "Make this bigger" beats "improve this section"
            </p>
          </div>
        </div>
      )
    },
    {
      id: 'polish',
      title: 'Step 4: Adding Polish',
      subtitle: 'Professional Touches',
      type: 'content',
      icon: <Sparkles className="w-16 h-16" />,
      content: (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div className="bg-gradient-to-br from-emerald-500/20 to-teal-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
              <div className="flex items-center gap-3 mb-4">
                <div className="bg-emerald-500 p-2 rounded-lg">
                  <Globe className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold">SEO & Meta Tags</h3>
              </div>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• Proper page titles</li>
                <li>• Meta descriptions</li>
                <li>• Open Graph tags for social media</li>
                <li>• Favicon</li>
              </ul>
            </div>

            <div className="bg-gradient-to-br from-blue-500/20 to-cyan-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
              <div className="flex items-center gap-3 mb-4">
                <div className="bg-blue-500 p-2 rounded-lg">
                  <Code className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold">Typography</h3>
              </div>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• Google Fonts integration</li>
                <li>• Font pairing for headers/body</li>
                <li>• Readable line heights</li>
                <li>• Proper font weights</li>
              </ul>
            </div>

            <div className="bg-gradient-to-br from-purple-500/20 to-pink-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
              <div className="flex items-center gap-3 mb-4">
                <div className="bg-purple-500 p-2 rounded-lg">
                  <Sparkles className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold">Micro-interactions</h3>
              </div>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• Smooth hover states</li>
                <li>• Button transitions</li>
                <li>• Back to top button</li>
                <li>• Active nav highlighting</li>
              </ul>
            </div>

            <div className="bg-gradient-to-br from-orange-500/20 to-red-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
              <div className="flex items-center gap-3 mb-4">
                <div className="bg-orange-500 p-2 rounded-lg">
                  <Check className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold">Accessibility</h3>
              </div>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• ARIA labels</li>
                <li>• Keyboard navigation</li>
                <li>• Color contrast ratios</li>
                <li>• Alt text for images</li>
              </ul>
            </div>
          </div>

          <div className="bg-gradient-to-r from-indigo-500/20 to-purple-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
            <h3 className="text-lg font-bold mb-4">⚡ Performance Optimization</h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="text-sm">
                <p className="font-semibold mb-1">Minify CSS</p>
                <p className="opacity-80">Reduce file size</p>
              </div>
              <div className="text-sm">
                <p className="font-semibold mb-1">Lazy Load Images</p>
                <p className="opacity-80">Faster initial load</p>
              </div>
              <div className="text-sm">
                <p className="font-semibold mb-1">Remove Unused CSS</p>
                <p className="opacity-80">Cleaner codebase</p>
              </div>
            </div>
          </div>
        </div>
      )
    },
    {
      id: 'deployment',
      title: 'Step 5: GitHub Pages',
      subtitle: 'Free Hosting Forever',
      type: 'content',
      icon: <Rocket className="w-16 h-16" />,
      content: (
        <div className="space-y-6">
          <div className="bg-gradient-to-br from-gray-700 to-gray-900 p-8 rounded-2xl border border-white/20">
            <div className="flex items-center gap-4 mb-6">
              <Github className="w-12 h-12" />
              <div>
                <h3 className="text-2xl font-bold">GitHub Pages</h3>
                <p className="opacity-80">Professional hosting at $0</p>
              </div>
            </div>

            <div className="space-y-4">
              <div className="flex items-start gap-4">
                <div className="bg-blue-500 min-w-[2.5rem] h-10 rounded-full flex items-center justify-center font-bold">1</div>
                <div className="flex-1 pt-2">
                  <h4 className="font-bold mb-2">Create Repository</h4>
                  <p className="text-sm opacity-90">Name it: <code className="bg-black/30 px-2 py-1 rounded">username.github.io</code></p>
                </div>
              </div>

              <div className="flex items-start gap-4">
                <div className="bg-purple-500 min-w-[2.5rem] h-10 rounded-full flex items-center justify-center font-bold">2</div>
                <div className="flex-1 pt-2">
                  <h4 className="font-bold mb-2">Upload Files</h4>
                  <p className="text-sm opacity-90">index.html, CSS, JS, and images folder</p>
                </div>
              </div>

              <div className="flex items-start gap-4">
                <div className="bg-pink-500 min-w-[2.5rem] h-10 rounded-full flex items-center justify-center font-bold">3</div>
                <div className="flex-1 pt-2">
                  <h4 className="font-bold mb-2">Enable Pages</h4>
                  <p className="text-sm opacity-90">Settings → Pages → Select main branch</p>
                </div>
              </div>

              <div className="flex items-start gap-4">
                <div className="bg-green-500 min-w-[2.5rem] h-10 rounded-full flex items-center justify-center font-bold">4</div>
                <div className="flex-1 pt-2">
                  <h4 className="font-bold mb-2">Live in Minutes</h4>
                  <p className="text-sm opacity-90">Your site is now accessible worldwide</p>
                </div>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-gradient-to-br from-green-500/20 to-emerald-500/20 backdrop-blur p-5 rounded-xl border border-white/10">
              <h4 className="font-bold mb-2 flex items-center gap-2">
                <Check className="w-5 h-5" />
                Benefits
              </h4>
              <ul className="space-y-1 text-sm opacity-90">
                <li>• Completely free</li>
                <li>• Automatic HTTPS</li>
                <li>• Fast CDN delivery</li>
                <li>• Auto-deploy on updates</li>
              </ul>
            </div>

            <div className="bg-gradient-to-br from-blue-500/20 to-indigo-500/20 backdrop-blur p-5 rounded-xl border border-white/10">
              <h4 className="font-bold mb-2 flex items-center gap-2">
                <Globe className="w-5 h-5" />
                Custom Domain
              </h4>
              <p className="text-sm opacity-90">
                Optional: Use your own domain name with simple DNS configuration
              </p>
            </div>
          </div>
        </div>
      )
    },
    {
      id: 'tips',
      title: 'Tips for Success',
      subtitle: 'Working Effectively with Claude',
      type: 'content',
      icon: <Lightbulb className="w-16 h-16" />,
      content: (
        <div className="space-y-5">
          {[
            {
              icon: <Code className="w-6 h-6" />,
              title: 'Be Specific',
              bad: 'Make it look better',
              good: 'Increase section spacing to 80px and make heading font 36px',
              color: 'from-red-500/20 to-orange-500/20'
            },
            {
              icon: <Sparkles className="w-6 h-6" />,
              title: 'Iterate in Steps',
              bad: 'Change everything at once',
              good: 'Make one change, review, then move to next',
              color: 'from-orange-500/20 to-yellow-500/20'
            },
            {
              icon: <MessageSquare className="w-6 h-6" />,
              title: 'Ask Why',
              bad: 'Just accept the code',
              good: 'Why did you use flexbox instead of grid here?',
              color: 'from-yellow-500/20 to-green-500/20'
            },
            {
              icon: <Monitor className="w-6 h-6" />,
              title: 'Test Thoroughly',
              bad: 'Assume it works everywhere',
              good: 'Test on mobile, tablet, desktop, different browsers',
              color: 'from-green-500/20 to-cyan-500/20'
            }
          ].map((tip, i) => (
            <div key={i} className={`bg-gradient-to-r ${tip.color} backdrop-blur p-6 rounded-2xl border border-white/10`}>
              <div className="flex items-start gap-4">
                <div className="bg-white/20 p-3 rounded-full mt-1">
                  {tip.icon}
                </div>
                <div className="flex-1">
                  <h4 className="text-xl font-bold mb-3">{tip.title}</h4>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <p className="text-xs font-semibold opacity-60 mb-1">❌ DON'T</p>
                      <p className="text-sm bg-black/20 p-3 rounded-lg">{tip.bad}</p>
                    </div>
                    <div>
                      <p className="text-xs font-semibold opacity-60 mb-1">✅ DO</p>
                      <p className="text-sm bg-black/20 p-3 rounded-lg">{tip.good}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )
    },
    {
      id: 'limitations',
      title: 'Know the Limits',
      subtitle: 'What Claude Does Best',
      type: 'content',
      icon: <AlertCircle className="w-16 h-16" />,
      content: (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-gradient-to-br from-green-500/20 to-emerald-500/20 backdrop-blur p-6 rounded-2xl border border-green-500/30">
              <h3 className="text-xl font-bold mb-4 text-green-400">✓ Claude Excels At</h3>
              <ul className="space-y-2 text-sm opacity-90">
                <li>✓ HTML, CSS, JavaScript creation</li>
                <li>✓ Responsive design implementation</li>
                <li>✓ Animations and interactions</li>
                <li>✓ Content structure and layout</li>
                <li>✓ Debugging code issues</li>
                <li>✓ Explaining technical concepts</li>
                <li>✓ Portfolio and business sites</li>
              </ul>
            </div>

            <div className="bg-gradient-to-br from-orange-500/20 to-red-500/20 backdrop-blur p-6 rounded-2xl border border-orange-500/30">
              <h3 className="text-xl font-bold mb-4 text-orange-400">⚠️ Beyond Basic Scope</h3>
              <ul className="space-y-2 text-sm opacity-90">
                <li>• Complex backend systems</li>
                <li>• Database management</li>
                <li>• User authentication systems</li>
                <li>• E-commerce functionality</li>
                <li>• Payment processing</li>
                <li>• Advanced server configs</li>
                <li>• Complex web applications</li>
              </ul>
            </div>
          </div>

          <div className="bg-blue-500/20 backdrop-blur p-6 rounded-2xl border border-blue-500/30">
            <h3 className="text-lg font-bold mb-3 flex items-center gap-2">
              <Check className="w-6 h-6" />
              Perfect For Most Projects
            </h3>
            <p className="opacity-90">
              For portfolio sites, landing pages, business websites, and most informational sites, Claude can handle the entire build. 
              If you need complex web applications with databases and user accounts, you'll need additional development resources.
            </p>
          </div>

          <div className="bg-gradient-to-r from-purple-500/20 to-pink-500/20 backdrop-blur p-6 rounded-2xl border border-white/10">
            <h3 className="text-lg font-bold mb-3">💡 Pro Approach</h3>
            <p className="opacity-90">
              Use Claude for frontend excellence, combine with other tools for backend needs. 
              The combination of Claude + simple services (like Formspree for forms) covers 90% of use cases.
            </p>
          </div>
        </div>
      )
    },
    {
      id: 'result',
      title: 'The Final Result',
      subtitle: 'Professional Portfolio in Hours',
      type: 'content',
      icon: <Check className="w-16 h-16" />,
      content: (
        <div className="space-y-6">
          <div className="bg-gradient-to-br from-indigo-600/40 to-purple-600/40 backdrop-blur-xl p-8 rounded-3xl border border-white/20 text-center">
            <Globe className="w-16 h-16 mx-auto mb-4 opacity-80" />
            <h3 className="text-3xl font-bold mb-2">bradcoles-dev.github.io</h3>
            <p className="text-lg opacity-80">Live & Production Ready</p>
            
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8">
              <div className="bg-white/10 backdrop-blur p-4 rounded-xl">
                <p className="text-3xl font-bold mb-1">4-5</p>
                <p className="text-sm opacity-80">Hours Total</p>
              </div>
              <div className="bg-white/10 backdrop-blur p-4 rounded-xl">
                <p className="text-3xl font-bold mb-1">$0</p>
                <p className="text-sm opacity-80">Hosting Cost</p>
              </div>
              <div className="bg-white/10 backdrop-blur p-4 rounded-xl">
                <p className="text-3xl font-bold mb-1">100%</p>
                <p className="text-sm opacity-80">Responsive</p>
              </div>
              <div className="bg-white/10 backdrop-blur p-4 rounded-xl">
                <p className="text-3xl font-bold mb-1">∞</p>
                <p className="text-sm opacity-80">Updates</p>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-gradient-to-br from-green-500/20 to-teal-500/20 backdrop-blur p-6 rounded-xl border border-white/10">
              <h4 className="font-bold mb-3 flex items-center gap-2">
                <Monitor className="w-5 h-5" />
                Key Features Delivered
              </h4>
              <ul className="space-y-2 text-sm opacity-90">
                <li>✓ Smooth scrolling navigation</li>
                <li>✓ Mobile hamburger menu</li>
                <li>✓ Interactive skill cards</li>
                <li>✓ Working contact form</li>
                <li>✓ Scroll animations</li>
                <li>✓ SEO optimized</li>
              </ul>
            </div>

            <div className="bg-gradient-to-br from-blue-500/20 to-indigo-500/20 backdrop-blur p-6 rounded-xl border border-white/10">
              <h4 className="font-bold mb-3 flex items-center gap-2">
                <Smartphone className="w-5 h-5" />
                Professional Quality
              </h4>
              <ul className="space-y-2 text-sm opacity-90">
                <li>✓ Clean, modern design</li>
                <li>✓ Fast loading times</li>
                <li>✓ Accessible to all users</li>
                <li>✓ Easy to maintain</li>
                <li>✓ Custom domain ready</li>
                <li>✓ Analytics ready</li>
              </ul>
            </div>
          </div>

          <div className="bg-gradient-to-r from-yellow-500/20 to-orange-500/20 backdrop-blur border-l-4 border-yellow-500 p-6 rounded-r-2xl">
            <p className="font-semibold mb-2 flex items-center gap-2">
              <Sparkles className="w-5 h-5" />
              The Best Part?
            </p>
            <p className="opacity-90">
              No coding experience required. Just clear communication, iteration, and patience. 
              AI has truly democratized web development.
            </p>
          </div>
        </div>
      )
    },
    {
      id: 'outro',
      title: 'Ready to Build Yours?',
      subtitle: "Let's Get Started",
      type: 'cover',
      icon: <Rocket className="w-24 h-24" />,
      content: (
        <div className="text-center space-y-8">
          <div className="space-y-4">
            <p className="text-xl font-light opacity-90">
              You now have everything you need to build your own professional portfolio
            </p>
            <p className="text-lg opacity-70">
              No excuses. No barriers. Just you and Claude.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-8">
            <div className="bg-white/10 backdrop-blur p-6 rounded-2xl">
              <div className="text-4xl mb-3">📝</div>
              <h4 className="font-bold mb-2">Plan</h4>
              <p className="text-sm opacity-80">Define your goals & gather content</p>
            </div>
            <div className="bg-white/10 backdrop-blur p-6 rounded-2xl">
              <div className="text-4xl mb-3">💬</div>
              <h4 className="font-bold mb-2">Collaborate</h4>
              <p className="text-sm opacity-80">Work iteratively with Claude</p>
            </div>
            <div className="bg-white/10 backdrop-blur p-6 rounded-2xl">
              <div className="text-4xl mb-3">🚀</div>
              <h4 className="font-bold mb-2">Deploy</h4>
              <p className="text-sm opacity-80">Launch on GitHub Pages</p>
            </div>
          </div>

          <div className="pt-8 space-y-3">
            <p className="text-xl font-semibold">Drop your portfolio link in the comments!</p>
            <p className="opacity-80">Like, Subscribe & Hit the Bell 🔔</p>
            <p className="text-3xl mt-4">Cheers! 🇦🇺</p>
          </div>
        </div>
      )
    }
  ];

  const nextSlide = () => {
    if (currentSlide < slides.length - 1) {
      setCurrentSlide(currentSlide + 1);
    }
  };

  const prevSlide = () => {
    if (currentSlide > 0) {
      setCurrentSlide(currentSlide - 1);
    }
  };

  const currentSlideData = slides[currentSlide];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white font-sans">
      {/* Progress Bar */}
      <div className="fixed top-0 left-0 right-0 h-1 bg-white/10 z-50">
        <div 
          className="h-full bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-600 transition-all duration-300"
          style={{ width: `${progress}%` }}
        />
      </div>

      {/* Main Content */}
      <div className="container mx-auto px-4 py-8 min-h-screen flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between mb-8 pt-4">
          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-r from-cyan-400 to-blue-600 p-3 rounded-xl">
              <Home className="w-6 h-6" />
            </div>
            <div>
              <h1 className="text-2xl font-bold">Portfolio Tutorial</h1>
              <p className="text-sm opacity-60">With Claude AI</p>
            </div>
          </div>
          <div className="text-right">
            <p className="text-sm opacity-60">Slide {currentSlide + 1} of {slides.length}</p>
          </div>
        </div>

        {/* Slide Content */}
        <div className="flex-1 flex items-center justify-center">
          <div className="w-full max-w-6xl">
            <div className="mb-8 text-center">
              <div className="flex items-center justify-center mb-6 opacity-80">
                {currentSlideData.icon}
              </div>
              <h2 className="text-5xl md:text-6xl font-bold mb-3 bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-600 bg-clip-text text-transparent">
                {currentSlideData.title}
              </h2>
              <p className="text-2xl opacity-70">{currentSlideData.subtitle}</p>
            </div>

            <div className="bg-white/5 backdrop-blur-xl rounded-3xl p-8 md:p-12 border border-white/10 shadow-2xl">
              {currentSlideData.content}
            </div>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex items-center justify-between mt-8 pb-4">
          <button
            onClick={prevSlide}
            disabled={currentSlide === 0}
            className="flex items-center gap-2 px-6 py-3 bg-white/10 hover:bg-white/20 disabled:opacity-30 disabled:cursor-not-allowed rounded-xl backdrop-blur transition-all"
          >
            <ChevronLeft className="w-5 h-5" />
            Previous
          </button>

          <div className="flex gap-2">
            {slides.map((_, index) => (
              <button
                key={index}
                onClick={() => setCurrentSlide(index)}
                className={`w-2 h-2 rounded-full transition-all ${
                  index === currentSlide 
                    ? 'bg-blue-500 w-8' 
                    : 'bg-white/30 hover:bg-white/50'
                }`}
              />
            ))}
          </div>

          <button
            onClick={nextSlide}
            disabled={currentSlide === slides.length - 1}
            className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 disabled:opacity-30 disabled:cursor-not-allowed rounded-xl backdrop-blur transition-all"
          >
            Next
            <ChevronRight className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
}
