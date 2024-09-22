# Please read "Usage" first in the Read Me!
# You can use this script to easily create hundreds/thousands of WebClips.
# To start copy and paste the entire <dict> block within the <array> to a text file named "mobileConfig.txt" and set the vaule of <key>PayloadIdentifier</key> to "[ID]" and the vaule of <key>PayloadUUID</key> to "[UUID]".
# Now run and you will recieve your .mobileconfig file, from there add the following necessary code to the top:

# <?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
# <plist version="1.0">
# <dict>
#    <key>PayloadContent</key>
#    <array>

# And add the following to the bottom:

# </array>
# </dict>
# </plist>

# Perfect, your configuration profile is now ready to be tested!

import uuid

def generate_unique_id():
    return f"com.webclip.profile.{uuid.uuid4().hex[:8]}"

def main():
    try:
        with open("mobileConfig.txt", "r") as file:
            template = file.read()
    except FileNotFoundError:
        print("Error: mobileConfig.txt file not found.")
        return
    except IOError:
        print("Error: Unable to read mobileConfig.txt file.")
        return

    try:
        num_copies = int(input("How many WebClips do you want? "))
    except ValueError:
        print("Please enter a valid number of WebClips.")
        return

    with open("configurationProfile.mobileconfig", "w") as outfile:
        for i in range(num_copies):
            new_uuid = str(uuid.uuid4())
            new_id = generate_unique_id()

            modified_text = template.replace("[UUID]", new_uuid).replace("[ID]", new_id)

            outfile.write(modified_text + "\n")

    print(f"\nYour mobile configuration profile has been saved to configurationProfile.mobileconfig")

if __name__ == "__main__":
    main()
