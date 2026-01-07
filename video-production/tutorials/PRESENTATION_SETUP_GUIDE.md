# Interactive Presentation Setup Guide
## How to use the portfolio_tutorial.jsx presentation for screen recording

---

## 🎯 Quick Start

You have **TWO OPTIONS** for displaying the interactive presentation:

### Option 1: Use the Ready-Made HTML File (Easiest)
✅ **Recommended for screen recording**

1. Open **[presentation_setup.html](presentation_setup.html)** in your browser
2. Press **F11** for fullscreen
3. Use arrow keys to navigate (→ next, ← previous)
4. Start recording with OBS Studio!

**Pros**: Works immediately, no setup required
**Cons**: Only shows first 2 slides (demo version)

---

### Option 2: Use Claude Artifacts (Full Presentation)
✅ **Recommended for the complete 10-slide presentation**

1. Go to https://claude.ai
2. Start a new conversation
3. Copy the entire **[portfolio_tutorial.jsx](portfolio_tutorial.jsx)** file
4. Paste it and ask: "Please display this React component as an Artifact"
5. Claude will render the interactive presentation
6. Click the "Expand" button in the artifact to go fullscreen
7. Start recording!

**Pros**: Full 10-slide presentation, beautiful rendering
**Cons**: Requires Claude.ai account

---

## 🎬 Recording Setup

### Before You Start:

1. **Set Screen Resolution**: 1920x1080
2. **Clear Browser**: Use incognito/private mode for clean interface
3. **Hide Bookmarks Bar**: View → Hide bookmarks bar
4. **Close Other Apps**: Minimize distractions
5. **Test OBS**: Do a 10-second test recording

### OBS Studio Setup:

```
Scene Setup:
├── Source 1: Browser Window Capture
│   └── Select your browser window
├── Resolution: 1920x1080
├── FPS: 30
└── Bitrate: 8000-12000 kbps
```

### Recording Each Slide:

1. **Navigate to slide** using arrow keys
2. **Let it sit** for 5-10 seconds (viewers need time to read)
3. **Move to next slide** with smooth transition
4. **Record 2-3 takes** of each slide for options

---

## ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| `→` | Next slide |
| `←` | Previous slide |
| `F11` | Fullscreen (highly recommended) |
| `Esc` | Exit fullscreen |
| `H` | Toggle help overlay (HTML version only) |
| `Click dots` | Jump to specific slide |

---

## 📋 Slide List & Recording Times

### Slide 1: Intro (30 seconds)
- **What to show**: Title, subtitle, duration badges
- **Recording tip**: Hold steady, this is your hook

### Slide 2: Planning (45 seconds)
- **What to show**: 4 planning cards + pro tip
- **Recording tip**: Slow pan across cards so viewers can read

### Slide 3: First Conversation (30 seconds)
- **What to show**: Example prompt + best practices
- **Recording tip**: Zoom in slightly on the code example

### Slide 4: Iterative Refinement (60 seconds)
- **What to show**: 6 iteration rounds
- **Recording tip**: This is dense - hold for full 60 seconds

### Slide 5: Adding Polish (45 seconds)
- **What to show**: 4 polish categories + performance tips
- **Recording tip**: Highlight the micro-interactions section

### Slide 6: GitHub Pages (45 seconds)
- **What to show**: Deployment steps + benefits
- **Recording tip**: Emphasize the "free forever" aspect

### Slide 7: Tips for Success (60 seconds)
- **What to show**: 4 tips with DO/DON'T examples
- **Recording tip**: Viewers will want to screenshot this one

### Slide 8: Limitations (45 seconds)
- **What to show**: What Claude excels at vs. beyond scope
- **Recording tip**: Balance is key - be honest but encouraging

### Slide 9: Final Result (30 seconds)
- **What to show**: Stats and features delivered
- **Recording tip**: This is your victory lap - make it feel rewarding

### Slide 10: Outro (30 seconds)
- **What to show**: Call to action, subscribe, cheers
- **Recording tip**: End on the "Cheers! 🇦🇺" for Australian vibe

**Total presentation recording time**: ~6-7 minutes

---

## 🎨 Visual Quality Tips

### For Best Results:

1. **Fullscreen Mode**: Always record in fullscreen (F11)
2. **High Resolution**: Ensure browser is displaying at 1920x1080
3. **Smooth Movements**: If panning, move cursor slowly and steadily
4. **Zoom Carefully**: If zooming in, use browser zoom (Ctrl/Cmd + +/-)
5. **Cursor Visibility**: Consider hiding cursor for cleaner look (optional)

### Color & Brightness:

- The presentation uses dark mode with vibrant gradients
- Looks best on displays with good color accuracy
- If recording looks washed out, increase contrast in OBS

### Text Readability:

- All text is designed to be readable at 1080p
- Test by playing back a few seconds
- If text is blurry, check OBS bitrate settings

---

## 🔧 Troubleshooting

### Issue: Presentation doesn't load
**Solution**:
- Check internet connection (CDN dependencies)
- Try a different browser (Chrome recommended)
- Clear cache and reload

### Issue: Slides look different from expected
**Solution**:
- The HTML demo only has 2 slides
- Use Claude Artifacts for full 10-slide version
- Check that Tailwind CSS is loading (view source)

### Issue: Keyboard navigation not working
**Solution**:
- Click once on the presentation to focus
- Ensure you're not in browser's address bar
- Try refreshing the page

### Issue: Fullscreen cuts off content
**Solution**:
- Zoom out browser (Ctrl/Cmd + -)
- Adjust screen resolution
- Use a smaller browser window in OBS

---

## 📦 Alternative: Export as Video

If you want to pre-render the presentation:

### Using Screen Recording Software:

**macOS**:
```bash
# Use QuickTime Player
File → New Screen Recording
```

**Windows**:
```bash
# Use built-in Xbox Game Bar
Windows Key + G → Record
```

**Linux**:
```bash
# Use SimpleScreenRecorder or Kazam
```

### Settings for Export:
- Format: MP4
- Resolution: 1920x1080
- Frame Rate: 30fps
- Quality: High

---

## 🎯 Pro Recording Workflow

### Recommended Approach:

**Day 1: Setup & Test**
1. Set up OBS Studio
2. Load presentation in browser
3. Do test recordings
4. Review and adjust settings

**Day 2: Record Slides**
1. Record Slides 1-5
2. Take breaks between takes
3. Review each recording
4. Re-record any issues

**Day 3: Complete Recording**
1. Record Slides 6-10
2. Final review of all slides
3. Export organized files
4. Back up everything

### File Naming Convention:

```
slides_01_intro.mp4
slides_02_planning.mp4
slides_03_first_conversation.mp4
slides_04_iteration.mp4
slides_05_polish.mp4
slides_06_deployment.mp4
slides_07_tips.mp4
slides_08_limitations.mp4
slides_09_result.mp4
slides_10_outro.mp4
```

---

## ✅ Pre-Recording Checklist

Before you start recording:

- [ ] Screen resolution: 1920x1080
- [ ] Browser in fullscreen (F11)
- [ ] Incognito/private mode
- [ ] Bookmarks bar hidden
- [ ] Notifications disabled
- [ ] OBS settings verified
- [ ] Test recording completed
- [ ] Presentation loads correctly
- [ ] Keyboard controls work
- [ ] Backup plan ready (alternative browser/method)

---

## 🚀 Quick Commands

### For Claude Artifacts Method:

```
Prompt to use in Claude.ai:

"Please display this React component as an interactive artifact.
I need to record it for a YouTube tutorial, so make it fullscreen-friendly."

[Paste portfolio_tutorial.jsx content]
```

### For HTML Method:

```bash
# Simply open in browser:
# Double-click presentation_setup.html
# Or drag file into browser window
# Press F11 for fullscreen
# Start recording!
```

---

## 💡 Next Steps

After recording all slides:

1. ✅ Save all recordings to `raw-footage/slides/`
2. ✅ Generate AI voiceover (use voiceover_ai_sections.md)
3. ✅ Record Claude interactions (use screen_recording_shot_list.md)
4. ✅ Proceed to video editing phase

---

## 📞 Need Help?

### Common Questions:

**Q: Do I need all 10 slides?**
A: Yes, for the complete tutorial. But you can start with the HTML demo to test your recording setup.

**Q: Can I edit the presentation?**
A: Yes! Edit portfolio_tutorial.jsx and re-load in Claude Artifacts.

**Q: What if I don't have Claude.ai access?**
A: Use the HTML version and manually create remaining slides, or record what you can and edit creatively.

**Q: How long will this take?**
A: Setup: 30 mins, Recording: 2-3 hours (with retakes), Review: 30 mins

---

Ready to record? Open **[presentation_setup.html](presentation_setup.html)** or load **[portfolio_tutorial.jsx](portfolio_tutorial.jsx)** in Claude Artifacts and let's go! 🎬
