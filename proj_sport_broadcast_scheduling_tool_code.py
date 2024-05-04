import streamlit as st
import json
import os

class SportsBroadcastSchedulingTool:
    def __init__(self):
        self.data = {}
        self.load_event_data()

    def load_event_data(self):
        if os.path.exists("event_data.json"):  # Check if the file exists
            with open("event_data.json", "r") as file:
                self.data = json.load(file)

    def save_event_data(self):
        with open("event_data.json", "w") as file:
            json.dump(self.data, file)

    def add_event(self, time, date, location, team, team_leader):
        if str(date) in self.data:
            events = self.data[str(date)]
            # Check if any event has the same time
            if any(event["time"] == time for event in events):
                return False
            else:
                # Append the new event to the existing events for the date
                events.append({"time": time, "location": location, "team": team, "team_leader": team_leader})
        else:
            # If there are no events for the date, create a new list with the event
            self.data[str(date)] = [{"time": time, "location": location, "team": team, "team_leader": team_leader}]
        self.save_event_data()
        return True

    def update_event(self, selected_date, event_idx, time, location, team, team_leader):
        events = self.data.get(str(selected_date), [])
        events[event_idx] = {"time": time, "location": location, "team": team, "team_leader": team_leader}
        self.save_event_data()

    def delete_event(self, selected_date, event_idx):
        events = self.data.get(str(selected_date), [])
        del events[event_idx]
        if not events:  # If no events left for the date, remove the date key from data
            del self.data[str(selected_date)]
        self.save_event_data()

    def get_events_for_date(self, selected_date):
        return self.data.get(str(selected_date), [])  # Return empty list if date not found

    def show_event_details(self, selected_date):
        events = self.get_events_for_date(selected_date)
        if events:
            st.write(f"Events on {selected_date}:")
            for i, event in enumerate(events, 1):
                st.write(f"{i}) Time: {event['time']}")
                st.write(f"   Location: {event['location']}")
                st.write(f"   Team: {event['team']}")
                st.write(f"   Team Leader: {event['team_leader']}")
                st.write("---")
        else:
            st.warning("No events scheduled for this date.")

    def feedback(self, feedback_text):
        # Here you can implement your logic to handle the feedback, such as sending it to a database or email
        pass

def main():
    st.title("Sports Broadcast Scheduling Tool")
    app = SportsBroadcastSchedulingTool()

    selected_date = st.date_input("Select Date")

    # Display the image
    # Use the provided image path
    image_path = r"C:\Users\sagar\Downloads\sport.jpg"  # Using raw string literal to handle backslashes
    if os.path.exists(image_path):
        st.image(image_path, caption="Your Image Caption", use_column_width=True)
    else:
        st.warning("Image not found.")

    col1, col2 = st.columns(2)
    menu = col1.selectbox("Menu", ["Add Event", "Update Event", "Delete Event", "Show Event Details", "Feedback"])

    if menu == "Add Event":
        with col2:
            st.subheader("Add Event")
            time = st.text_input("Time:")
            location = st.text_input("Location:")
            team = st.text_input("Team:")
            team_leader = st.text_input("Team Leader:")
            if st.button("Save") and selected_date:
                if app.add_event(time, selected_date, location, team, team_leader):
                    st.success(f"Event added for {selected_date} at {time}.")
                else:
                    st.error(f"Time slot {time} is already occupied for {selected_date}.")

    elif menu == "Update Event":
        with col2:
            st.subheader("Update Event")
            if selected_date:
                events = app.get_events_for_date(selected_date)
                if events:
                    event_idx = st.selectbox("Select Event", range(len(events)), format_func=lambda x: f"Event {x+1}")
                    event = events[event_idx]
                    time = st.text_input("Time:", value=event["time"])
                    location = st.text_input("Location:", value=event["location"])
                    team = st.text_input("Team:", value=event["team"])
                    team_leader = st.text_input("Team Leader:", value=event["team_leader"])
                    if st.button("Update"):
                        app.update_event(selected_date, event_idx, time, location, team, team_leader)
                        st.success(f"Event updated for {selected_date}.")
                else:
                    st.warning("No event to update.")
            else:
                st.warning("Please select a date.")

    elif menu == "Delete Event":
        with col2:
            st.subheader("Delete Event")
            if selected_date:
                events = app.get_events_for_date(selected_date)
                if events:
                    event_idx = st.selectbox("Select Event", range(len(events)), format_func=lambda x: f"Event {x+1}")
                    if st.button("Delete"):
                        app.delete_event(selected_date, event_idx)
                        st.success(f"Event deleted for {selected_date}.")
                else:
                    st.warning("No event to delete.")
            else:
                st.warning("Please select a date.")

    elif menu == "Show Event Details":
        with col2:
            st.subheader("Event Details")
            if selected_date:
                app.show_event_details(selected_date)
            else:
                st.warning("Please select a date.")

    elif menu == "Feedback":
        with col2:
            st.subheader("Feedback")
            feedback_text = st.text_area("Enter your feedback or report any issues:")
            if st.button("Submit Feedback"):
                app.feedback(feedback_text)
                st.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()
