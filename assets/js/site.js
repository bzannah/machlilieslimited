(function () {
        "use strict";
        var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        var touch = window.matchMedia("(hover: none)").matches;

        /* ---------- PRELOADER ---------- */
        var loader = document.getElementById("loader");
        var ldNum = document.getElementById("ld-num");
        var ldFill = document.getElementById("ld-fill");
        var p = 0;
        function finishLoad() {
            document.body.classList.add("ready");
            startCounters();
        }
        if (reduce || !loader) {            // no preloader on subpages -> reveal instantly
            if (ldNum) ldNum.textContent = "100";
            if (ldFill) ldFill.style.width = "100%";
            if (loader) loader.classList.add("done");
            finishLoad();
        } else {
            var tick = setInterval(function () {
                p += Math.random() * 16 + 4;
                if (p >= 100) { p = 100; clearInterval(tick); setTimeout(function () { if (loader) loader.classList.add("done"); finishLoad(); }, 350); }
                if (ldNum) ldNum.textContent = Math.floor(p);
                if (ldFill) ldFill.style.width = p + "%";
            }, 140);
        }

        /* ---------- CUSTOM CURSOR ---------- */
        var dot = document.querySelector(".cursor-dot");
        var ring = document.querySelector(".cursor-ring");
        if (!touch && dot && ring) {
            var label = ring.querySelector(".c-label");
            var mx = window.innerWidth / 2, my = window.innerHeight / 2;
            var rx = mx, ry = my;
            document.addEventListener("mousemove", function (e) {
                mx = e.clientX; my = e.clientY;
                dot.style.transform = "translate(" + mx + "px," + my + "px) translate(-50%,-50%)";
            });
            (function loop() {
                rx += (mx - rx) * 0.16; ry += (my - ry) * 0.16;
                ring.style.transform = "translate(" + rx + "px," + ry + "px) translate(-50%,-50%)";
                requestAnimationFrame(loop);
            })();
            var hoverSel = "a, button, summary, .cap-row, .work-card, .quote, [data-cursor]";
            document.querySelectorAll(hoverSel).forEach(function (el) {
                el.addEventListener("mouseenter", function () {
                    var lbl = el.getAttribute("data-cursor");
                    if (el.classList.contains("work-card")) { ring.classList.add("is-label"); label.textContent = "View"; }
                    else { ring.classList.add("is-hover"); }
                });
                el.addEventListener("mouseleave", function () { ring.classList.remove("is-hover", "is-label"); });
            });
            document.addEventListener("mouseleave", function () { dot.style.opacity = 0; ring.style.opacity = 0; });
            document.addEventListener("mouseenter", function () { dot.style.opacity = 1; ring.style.opacity = 1; });
        }

        /* ---------- MAGNETIC ---------- */
        if (!touch && !reduce) {
            document.querySelectorAll(".magnetic").forEach(function (el) {
                var strength = 0.35;
                el.addEventListener("mousemove", function (e) {
                    var r = el.getBoundingClientRect();
                    var x = e.clientX - r.left - r.width / 2;
                    var y = e.clientY - r.top - r.height / 2;
                    el.style.transform = "translate(" + x * strength + "px," + y * strength + "px)";
                });
                el.addEventListener("mouseleave", function () { el.style.transform = "translate(0,0)"; });
            });
        }

        /* ---------- NAV (hide/condense + active) ---------- */
        var nav = document.getElementById("nav");
        var lastY = 0;
        function onScroll() {
            var y = window.scrollY;
            if (y > 40) nav.classList.add("scrolled"); else nav.classList.remove("scrolled");
            if (y > lastY && y > 400) nav.classList.add("hidden"); else nav.classList.remove("hidden");
            lastY = y;
            var prog = document.querySelector(".progress");
            var h = document.documentElement.scrollHeight - window.innerHeight;
            prog.style.width = (h > 0 ? (y / h) * 100 : 0) + "%";
        }
        window.addEventListener("scroll", onScroll, { passive: true });
        onScroll();

        /* active nav link via IntersectionObserver */
        var navMap = {};
        document.querySelectorAll(".nav-links a").forEach(function (a) {
            navMap[a.getAttribute("href").slice(1)] = a;
        });
        var secObs = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                var a = navMap[en.target.id];
                if (!a) return;
                if (en.isIntersecting) {
                    Object.keys(navMap).forEach(function (k) { navMap[k].classList.remove("active"); });
                    a.classList.add("active");
                }
            });
        }, { rootMargin: "-45% 0px -50% 0px" });
        ["work", "capabilities", "method", "studio"].forEach(function (id) {
            var s = document.getElementById(id); if (s) secObs.observe(s);
        });

        /* ---------- MOBILE MENU ---------- */
        var burger = document.getElementById("burger");
        var mobileMenu = document.getElementById("mobile-menu");
        if (burger) {
            burger.addEventListener("click", function () {
                var open = burger.classList.toggle("open");
                mobileMenu.classList.toggle("open", open);
                document.body.style.overflow = open ? "hidden" : "";
            });
            mobileMenu.querySelectorAll("a").forEach(function (a) {
                a.addEventListener("click", function () {
                    burger.classList.remove("open"); mobileMenu.classList.remove("open"); document.body.style.overflow = "";
                });
            });
        }

        /* ---------- REVEAL ON SCROLL ---------- */
        var revObs = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) { en.target.classList.add("in"); revObs.unobserve(en.target); }
            });
        }, { threshold: 0.14, rootMargin: "0px 0px -8% 0px" });
        document.querySelectorAll(".reveal").forEach(function (el) { revObs.observe(el); });

        /* ---------- COUNTERS ---------- */
        var countersDone = false;
        function startCounters() {
            if (countersDone) return; countersDone = true;
            document.querySelectorAll("[data-count]").forEach(function (el) {
                var target = parseFloat(el.getAttribute("data-count"));
                var suffix = el.getAttribute("data-suffix") || "";
                if (reduce) { el.textContent = target + suffix; return; }
                var t0 = null, dur = 1600;
                function step(ts) {
                    if (!t0) t0 = ts;
                    var prog = Math.min((ts - t0) / dur, 1);
                    var eased = 1 - Math.pow(1 - prog, 3);
                    el.textContent = Math.floor(eased * target) + suffix;
                    if (prog < 1) requestAnimationFrame(step); else el.textContent = target + suffix;
                }
                requestAnimationFrame(step);
            });
        }

        /* ---------- CAPABILITY PEEK ---------- */
        var peek = document.getElementById("cap-peek");
        if (!touch && peek) {
            var peekImg = peek.querySelector("img");
            var px = 0, py = 0, tx = 0, ty = 0, peekActive = false;
            document.querySelectorAll(".cap-row[data-peek]").forEach(function (row) {
                row.addEventListener("mouseenter", function () {
                    peekImg.src = row.getAttribute("data-peek");
                    peek.classList.add("show"); peekActive = true;
                });
                row.addEventListener("mouseleave", function () { peek.classList.remove("show"); peekActive = false; });
            });
            document.addEventListener("mousemove", function (e) { tx = e.clientX; ty = e.clientY; });
            (function peekLoop() {
                px += (tx - px) * 0.12; py += (ty - py) * 0.12;
                if (peekActive) { peek.style.left = px + "px"; peek.style.top = py + "px"; }
                requestAnimationFrame(peekLoop);
            })();
        }

        /* ---------- WORK CARD SPOTLIGHT ---------- */
        document.querySelectorAll(".work-card .work-media").forEach(function (media) {
            media.addEventListener("mousemove", function (e) {
                var r = media.getBoundingClientRect();
                media.style.setProperty("--mx", ((e.clientX - r.left) / r.width) * 100 + "%");
                media.style.setProperty("--my", ((e.clientY - r.top) / r.height) * 100 + "%");
            });
        });

        /* ---------- HERO LILY PARALLAX SWAY ---------- */
        var heroLily = document.getElementById("hero-lily");
        if (heroLily && !reduce && !touch) {
            document.addEventListener("mousemove", function (e) {
                var dx = (e.clientX / window.innerWidth - 0.5);
                var dy = (e.clientY / window.innerHeight - 0.5);
                heroLily.style.transform = "translateY(-50%) translate(" + dx * 30 + "px," + dy * 30 + "px) rotate(" + dx * 8 + "deg)";
            });
        }

        /* ---------- GENERATIVE PETAL CANVAS ---------- */
        var canvas = document.getElementById("petal-canvas");
        if (canvas && !reduce) {
            var ctx = canvas.getContext("2d");
            var W, H, dpr = Math.min(window.devicePixelRatio || 1, 2);
            var petals = [];
            var hero = document.querySelector(".hero");
            var mouseX = -999, mouseY = -999;

            function resize() {
                W = hero.offsetWidth; H = hero.offsetHeight;
                canvas.width = W * dpr; canvas.height = H * dpr;
                canvas.style.width = W + "px"; canvas.style.height = H + "px";
                ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            }
            function makePetals() {
                petals = [];
                var count = Math.min(70, Math.floor(W / 18));
                for (var i = 0; i < count; i++) {
                    petals.push({
                        x: Math.random() * W, y: Math.random() * H,
                        r: Math.random() * 2.2 + 0.6,
                        a: Math.random() * Math.PI * 2,
                        sp: Math.random() * 0.3 + 0.1,
                        sway: Math.random() * 0.02 + 0.005,
                        op: Math.random() * 0.5 + 0.15,
                        accent: Math.random() > 0.55
                    });
                }
            }
            function draw() {
                ctx.clearRect(0, 0, W, H);
                for (var i = 0; i < petals.length; i++) {
                    var pt = petals[i];
                    pt.a += pt.sway;
                    pt.y -= pt.sp;
                    pt.x += Math.sin(pt.a) * 0.4;
                    if (pt.y < -10) { pt.y = H + 10; pt.x = Math.random() * W; }
                    // gentle mouse repulsion
                    var dx = pt.x - mouseX, dy = pt.y - mouseY;
                    var d2 = dx * dx + dy * dy;
                    if (d2 < 14000) { var f = (14000 - d2) / 14000; pt.x += dx / Math.sqrt(d2 + 1) * f * 2.2; pt.y += dy / Math.sqrt(d2 + 1) * f * 2.2; }
                    ctx.beginPath();
                    ctx.arc(pt.x, pt.y, pt.r, 0, Math.PI * 2);
                    ctx.fillStyle = pt.accent ? "rgba(201,242,76," + pt.op + ")" : "rgba(241,235,220," + (pt.op * 0.5) + ")";
                    ctx.fill();
                }
                requestAnimationFrame(draw);
            }
            hero.addEventListener("mousemove", function (e) { var r = hero.getBoundingClientRect(); mouseX = e.clientX - r.left; mouseY = e.clientY - r.top; });
            hero.addEventListener("mouseleave", function () { mouseX = -999; mouseY = -999; });
            window.addEventListener("resize", function () { resize(); makePetals(); });
            resize(); makePetals(); draw();
        }

        /* ---------- YEAR ---------- */
        var yr = document.getElementById("year"); if (yr) yr.textContent = new Date().getFullYear();

        /* ---------- SMOOTH ANCHORS ---------- */
        document.querySelectorAll('a[href^="#"]').forEach(function (a) {
            a.addEventListener("click", function (e) {
                var id = this.getAttribute("href");
                if (id.length < 2) return;
                var t = document.querySelector(id);
                if (t) { e.preventDefault(); t.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" }); }
            });
        });

        /* ---------- ANALYTICS EVENTS (inert until GA_MEASUREMENT_ID is set) ---------- */
        document.querySelectorAll("[data-event]").forEach(function (el) {
            el.addEventListener("click", function () {
                if (!window.gtag) return;
                var name = el.getAttribute("data-event");
                var label = (el.getAttribute("data-label") || el.textContent || "").trim().slice(0, 80);
                try { gtag("event", name, { event_category: "engagement", event_label: label }); } catch (e) { }
            });
        });

        /* ---------- CONTACT FORM (progressive enhancement) ---------- */
        var ef = document.getElementById("enquiry-form");
        if (ef) {
            var fstatus = document.getElementById("form-status");
            var setStatus = function (msg, ok) {
                if (!fstatus) return;
                fstatus.textContent = msg;
                fstatus.className = "form-status show " + (ok ? "ok" : "err");
            };
            ef.addEventListener("submit", function (e) {
                if (!ef.checkValidity()) { ef.reportValidity(); return; }
                e.preventDefault();
                var data = {};
                Array.prototype.forEach.call(ef.elements, function (el) {
                    if (el.name && el.value && el.type !== "submit") data[el.name] = el.value;
                });
                if (window.gtag) { try { gtag("event", "form_submit", { event_category: "contact" }); } catch (e2) { } }
                var endpoint = ef.getAttribute("data-endpoint");
                if (endpoint) {
                    setStatus("Sending…", true);
                    fetch(endpoint, {
                        method: "POST",
                        headers: { "Content-Type": "application/json", "Accept": "application/json" },
                        body: JSON.stringify(data)
                    }).then(function (r) {
                        if (!r.ok) throw 0;
                        ef.reset();
                        setStatus("Thank you — your enquiry is on its way. We reply within one business day.", true);
                    }).catch(function () {
                        setStatus("Something went wrong. Please email machlilieslimited@gmail.com directly.", false);
                    });
                } else {
                    var subject = "Agentic Operations enquiry — " + (data["Company"] || data["Name"] || "");
                    var body = Object.keys(data).filter(function (k) { return k.charAt(0) !== "_"; })
                        .map(function (k) { return k + ": " + data[k]; }).join("\n\n");
                    window.location.href = "mailto:machlilieslimited@gmail.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
                    setStatus("Opening your email client… if nothing happens, email machlilieslimited@gmail.com directly.", true);
                }
            });
        }
    })();
