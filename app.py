import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Page Config
st.set_page_config(page_title="OSINT Image Analyser", layout="wide")
st.title("🔍 OSINT Image Metadata Analyser")
st.markdown("---")

# Helper function to convert GPS DMS to Decimal Degrees
def get_decimal_from_dms(dms, ref):
    degrees = dms[0]
    minutes = dms[1]
    seconds = dms[2]
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

uploaded_file = st.file_uploader("Upload an image (JPG/JPEG)", type=["jpg", "jpeg"])

if uploaded_file:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with col2:
        exif_data = image._getexif()
        
        if exif_data:
            st.success("✅ Technical Metadata Found")
            
            # Extract GPS specifically for mapping
            gps_info = {}
            detailed_metadata = {}
            
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "GPSInfo":
                    for t in value:
                        sub_tag = GPSTAGS.get(t, t)
                        gps_info[sub_tag] = value[t]
                else:
                    detailed_metadata[tag] = value

            # If GPS is present, show coordinates and map link
            if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
                lat = get_decimal_from_dms(gps_info['GPSLatitude'], gps_info.get('GPSLatitudeRef', 'N'))
                lon = get_decimal_from_dms(gps_info['GPSLongitude'], gps_info.get('GPSLongitudeRef', 'E'))
                
                st.subheader("📍 Geolocation Identified")
                st.write(f"**Coordinates:** {lat:.6f}, {lon:.6f}")
                google_maps_url = f"https://www.google.com/maps?q={lat},{lon}"
                st.link_button("View on Google Maps", google_maps_url)
                
                # Show a simple Streamlit map
                st.map({"lat": [lat], "lon": [lon]})

            # Show the rest of the metadata in an expander
            with st.expander("See Raw Metadata Details"):
                for k, v in detailed_metadata.items():
                    st.write(f"**{k}**: {v}")
        
        else:
            st.warning("⚠️ No EXIF metadata found. This image was likely stripped.")
            st.subheader("🕵️ Visual OSINT Resources")
            st.info("Technical data is missing. Use these visual verification tools:")
            
            st.markdown("- [🔍 Google Lens](https://lens.google.com/uploadbyurl)")
            st.markdown("- [🖼️ Yandex Images](https://yandex.com/images/)")
            st.markdown("- [☀️ SunCalc](https://suncalc.org)")
            st.markdown("- [🏔️ PeakVisor](https://peakvisor.com/)")
            
            st.divider()
            st.write("**Investigator's Checklist:**")
            st.checkbox("Identify unique landmarks or architecture")
            st.checkbox("Examine flora/fauna (biolocation)")
            st.checkbox("Analyze shadow length for time of day")

