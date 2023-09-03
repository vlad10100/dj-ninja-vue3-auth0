import { callExternalApi } from './ExternalApiService'

const apiServerUrl = import.meta.env.VITE_API_SERVER_URL

export const getPublicResource = async () => {
  const config = {
    url: `${apiServerUrl}/api/public`,
    method: 'GET',
    headers: {
      'content-type': 'application/json'
    }
  }

  const { data, error } = await callExternalApi({ config })

  return {
    data: data || null,
    error
  }
}

export const getProtectedResource = async (accessToken) => {
  const config = {
    url: `${apiServerUrl}/api/protected`,
    method: 'GET',
    headers: {
      'content-type': 'application/json',
      Authorization: `Bearer ${accessToken}`
    }
  }

  const { data, error } = await callExternalApi({ config })

  return {
    data: data || null,
    error
  }
}

export const getAdminResource = async (accessToken) => {
  const config = {
    url: `${apiServerUrl}/api/admin`,
    method: 'GET',
    headers: {
      'content-type': 'application/json',
      Authorization: `Bearer ${accessToken}`
    }
  }

  const { data, error } = await callExternalApi({ config })

  return {
    data: data || null,
    error
  }
}
