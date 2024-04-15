def solution(times):
    ID_CHECK_DURATION = 5 * 60  # 5 minutes converted to seconds
    MAX_QUEUE_LENGTH = 10
    queue = []  # Queue to keep track of the finish times of people in the queue

    # Start processing from time of arrival of the first person
    current_time = times[0]
    for arrival_time in times:
        # Remove people from the queue who have finished their ID check
        while queue and queue[0] <= arrival_time:
            queue.pop(0)

        # Check if the queue is not full
        if len(queue) < MAX_QUEUE_LENGTH:
            if not queue:
                # If queue is empty, start ID check immediately
                finish_time = arrival_time + ID_CHECK_DURATION
            else:
                # Start ID check when the last person in the queue is done
                finish_time = max(queue[-1], arrival_time) + ID_CHECK_DURATION

            queue.append(finish_time)  # Add the finish time to the queue
            current_time = finish_time  # Update the current time
        else:
            # If the queue is full, the person leaves and we do nothing
            pass

    # The last finish time in the queue is when the last person is processed
    last_finish_time = queue[-1] if queue else current_time

    return last_finish_time

# Example usage:
times1 = [1, 6, 9, 502]
print(solution(times1))  # Expected output is 1201

times2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(solution(times2))  # Expected output is 3301
